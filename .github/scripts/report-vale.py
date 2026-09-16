#!/usr/bin/env python3
"""Turn a Vale JSON run into a job summary and a pull-request comment.

Nothing here blocks. Every glossary rule warns in this repo, so a finding has no
effect on the build and needs somewhere to appear or it is not a rule at all.

The findings are split by whether the pull request touched the file. A warning in
a file you edited is yours; the rest are the corpus as you found it. Without that
split the 49 warnings already in the archive would bury the one you added.
"""

import json
import os
import sys

MARKER = "<!-- nucleus-glossary-vale -->"
MAX_ROWS = 40


def load(path):
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        return {}
    with open(path) as fh:
        return json.load(fh) or {}


def rows(report, files):
    """Flatten Vale's {file: [alert]} into sorted rows, keeping only `files`."""
    out = []
    for path, alerts in report.items():
        if files is not None and path not in files:
            continue
        for a in alerts:
            # The span start disambiguates two hits on one line, which are two
            # findings and would otherwise render as one row repeated.
            out.append(
                (path, a["Line"], a["Span"][0], a["Check"], a["Match"], a["Message"])
            )
    return sorted(out)


def table(items):
    lines = ["| File | Line | Found | Rule |", "| --- | --- | --- | --- |"]
    for path, line, col, check, match, _msg in items[:MAX_ROWS]:
        kind = check.split(".", 1)[-1]
        lines.append(f"| `{path}` | {line}:{col} | `{match}` | {kind} |")
    if len(items) > MAX_ROWS:
        lines.append(f"\n…and {len(items) - MAX_ROWS} more.")
    return "\n".join(lines)


def suggestions(items):
    """One line per distinct swap, so the reader sees the ask not just the hit."""
    seen = {}
    for _p, _l, _c, _chk, match, msg in items:
        seen.setdefault(match, msg)
    return "\n".join(f"- {msg}" for _m, msg in sorted(seen.items()))


def main():
    report = load("vale.json")
    changed = set()
    if os.path.exists("changed.txt"):
        with open("changed.txt") as fh:
            changed = {ln.strip() for ln in fh if ln.strip()}

    mine = rows(report, changed)
    everything = rows(report, None)
    seen = set(mine)
    theirs = [r for r in everything if r not in seen]
    others = len(theirs)
    other_files = len({r[0] for r in theirs})

    # ---- job summary: the full picture ----
    parts = ["## Glossary check", ""]
    if not everything:
        parts.append("**No findings.** Nothing to report.")
    else:
        parts.append(
            f"**{len(everything)} warnings across {len({r[0] for r in everything})} files.** "
            "Nothing blocks. Every glossary rule warns here, because new vocabulary "
            "enters the program through DevNotes and blocking the source would stop "
            "the glossary growing."
        )
        parts += ["", "### In files this pull request touched", ""]
        parts.append(table(mine) if mine else "None.")
        if mine:
            parts += ["", suggestions(mine)]
        if others:
            parts += [
                "",
                "### Everywhere else",
                "",
                f"{others} warnings in {other_files} other files. These were here before "
                "this pull request and are listed for context only.",
                "",
                "<details><summary>Show them</summary>",
                "",
                table(theirs),
                "",
                "</details>",
            ]
    summary = "\n".join(parts) + "\n"

    step_summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if step_summary:
        with open(step_summary, "a") as fh:
            fh.write(summary)
    else:
        sys.stdout.write(summary)

    # ---- pull-request comment: only what this pull request is responsible for ----
    body = [MARKER, "## Glossary check", ""]
    if mine:
        body.append(
            f"**{len(mine)} warnings in files this pull request touched.** "
            "Nothing blocks — these are advisory."
        )
        body += ["", table(mine), "", suggestions(mine)]
    else:
        body.append("**No glossary findings in the files this pull request touched.**")
    if others:
        body.append(
            f"\n{others} pre-existing warnings elsewhere in the archive are listed in "
            "the job summary, not here."
        )
    body.append(
        "\nThe rules come from the shared Nucleus glossary. A wrong rule is a finding "
        "about the glossary — say so rather than reworking the sentence."
    )
    with open("comment.md", "w") as fh:
        fh.write("\n".join(body) + "\n")

    # Post a comment when this pull request has findings of its own. When it has
    # none, update an existing comment so a fixed pull request stops saying it is
    # dirty — but do not open one just to say nothing is wrong.
    gh_out = os.environ.get("GITHUB_OUTPUT")
    if gh_out:
        with open(gh_out, "a") as fh:
            fh.write(f"has_findings={'true' if mine else 'false'}\n")
    print(f"{len(mine)} findings in touched files, {others} elsewhere", file=sys.stderr)


if __name__ == "__main__":
    main()
