# Vendored from the Nucleus CDK, unmodified below this header.
#
#   source:  nucleus-cdk 0.6.0, cdk/calculators/naming.py
#   sha256:  a7db5089b07ef4887950f4313cde4cc2f4b57fb1982825636307eefad3b96e58
#   license: MIT (https://opensource.org/license/mit)
#   vendored: 2026-09-09
#
# Why this file exists: this DevNote pins nucleus-cdk==0.5.0rc2, which is the
# release that still carries the old plate-reader API
# (cdk.analysis.cytosol.platereader) every notebook here is written against.
# cdk.calculators.naming first appears in 0.6.0, which deleted that API — so no
# single CDK release provides both. The 8-factor figure needs these two helpers
# to add base master-mix concentrations back onto the titration values; without
# them the axes show titration-only concentrations. Copying the module keeps one
# environment and runs the upstream code rather than a reimplementation.
#
# Do not edit. To update, re-copy from a newer CDK and refresh the hash above.

"""Reagent column-name normalization utilities.

The discovery-plate pipeline accepts reagent column names in several
spellings — ``[PMix] (mg/mL)`` from one upstream tool, ``pmix mg/ml``
from another, ``PMix mg/mL`` hand-typed — and matches them against
``reagents.csv`` and ``fixed_rxn_concs.csv`` after canonicalization.
This module is the single source of truth for that canonicalization
so the pipeline calculator, ``doe.py`` generators, and the
orchestrator all agree on what counts as the same reagent.

Public surface:

- :func:`strip_wrapping_pairs` — peel ``[]``, ``()``, ``{}`` wrappers.
- :func:`normalize_reagent_name` — canonical reagent identifier (no
  punctuation, lower-case, with token aliases applied).
- :func:`normalize_unit` — canonical unit identifier (lower-case,
  micro-sign collapsed, whitespace stripped, punctuation kept).
- :func:`format_reagent_column_name` — build a ``"<reagent> <unit>"``
  column header.
- :func:`split_concentration_column_name` — inverse of the above:
  return ``(reagent, unit)`` from a column header, or ``None`` if the
  header doesn't carry a unit.
- :func:`column_key` — the canonical comparison key for a column
  header. Two columns with the same key represent the same reagent.
"""

from __future__ import annotations

import re
from typing import Any

import pandas as pd

# Token aliases applied during reagent-name normalization. Maps the
# common short/long forms onto a canonical token so e.g. ``amino_acids``
# and ``aas`` collapse to the same key.
_REAGENT_TOKEN_ALIASES: dict[str, str] = {
    "rnase": "rnas",
    "inhibitor": "inh",
    "inhib": "inh",
    "amino": "aas",
    "acids": "",
    "rxn": "reaction",
    "vol": "volume",
}

# Wrapper character pairs peeled by ``strip_wrapping_pairs``.
_WRAPPER_PAIRS: tuple[tuple[str, str], ...] = (
    ("(", ")"),
    ("[", "]"),
    ("{", "}"),
)


def strip_wrapping_pairs(text: str) -> str:
    """Remove repeated whole-string wrappers like ``[]`` or ``()``."""
    out = text.strip()
    while out:
        changed = False
        for left, right in _WRAPPER_PAIRS:
            if out.startswith(left) and out.endswith(right) and len(out) >= 2:
                out = out[1:-1].strip()
                changed = True
        if not changed:
            break
    return out


def normalize_reagent_name(name: str) -> str:
    """Canonicalize a reagent label for matching across files.

    Strips wrappers, lowercases, splits on any non-alphanumeric run,
    applies token aliases, and joins. ``"[PMix]"`` and ``"pmix"`` and
    ``"P-Mix"`` all collapse to ``"pmix"``.
    """
    stripped = strip_wrapping_pairs(str(name)).casefold()
    tokens = [tok for tok in re.split(r"[^a-z0-9]+", stripped) if tok]
    return "".join(_REAGENT_TOKEN_ALIASES.get(tok, tok) for tok in tokens)


def normalize_unit(unit: Any) -> str:
    """Canonicalize a unit label for tolerant unit equality.

    Strips wrappers, normalizes the micro-sign (``µ``/``μ``) to ``u``,
    lowercases, and removes whitespace. ``mg/mL`` and ``mg/ml`` both
    collapse to ``"mg/ml"``; ``µM`` and ``uM`` both collapse to
    ``"um"``.
    """
    if pd.isna(unit):
        return ""
    normalized = strip_wrapping_pairs(str(unit))
    normalized = normalized.replace("μ", "u").replace("µ", "u").casefold()
    return "".join(normalized.split())


def format_reagent_column_name(
    reagent: str, unit: str | None = None
) -> str:
    """Build a canonical ``"<reagent> <unit>"`` column header.

    Reagent and unit are kept in their input case (this is a
    presentation function — for matching, run through
    :func:`normalize_reagent_name` and :func:`normalize_unit`).
    """
    reagent_name = str(reagent).strip()
    if not reagent_name:
        raise ValueError("Reagent name cannot be empty.")

    if unit is None or pd.isna(unit):
        return reagent_name

    unit_name = str(unit).strip()
    if not unit_name:
        return reagent_name
    if reagent_name.endswith(f" {unit_name}"):
        return reagent_name
    return f"{reagent_name} {unit_name}"


def split_concentration_column_name(name: str) -> tuple[str, str] | None:
    """Parse a ``"<reagent> <unit>"`` column header.

    Returns ``(reagent, unit)`` or ``None`` if the header has no
    embedded unit. Uses ``rsplit`` because a reagent name may itself
    contain whitespace (``"amino acid solution"``) but the unit is
    always the last whitespace-delimited token.
    """
    text = str(name).strip()
    if " " not in text:
        return None
    reagent, unit = text.rsplit(" ", 1)
    reagent, unit = reagent.strip(), unit.strip()
    if not reagent or not unit:
        return None
    return reagent, unit


def column_key(name: str) -> tuple[str, str]:
    """Return the canonical comparison key for a column header.

    Two headers with the same return value name the same reagent.
    For headers with no unit, the unit half is the empty string.
    Headers with no embedded unit at all are treated as
    reagent-only — useful when matching against single-token headers
    like ``"vioC"`` that omit units.
    """
    parts = split_concentration_column_name(name)
    if parts is None:
        return normalize_reagent_name(name), ""
    reagent, unit = parts
    return normalize_reagent_name(reagent), normalize_unit(unit)


def format_bracketed_column_name(canonical_reagent: str, unit: str) -> str:
    """Return ``"[<canonical_reagent>] <unit>"``.

    The presentation form used in every CSV the orchestrator emits.
    Reagent is wrapped in square brackets; unit is kept verbatim
    (no parens added). Empty unit is allowed and yields just
    ``"[<canonical_reagent>]"``.
    """
    reagent = str(canonical_reagent).strip()
    if not reagent:
        raise ValueError("Reagent name cannot be empty.")
    unit_text = str(unit).strip() if unit is not None else ""
    if not unit_text:
        return f"[{reagent}]"
    return f"[{reagent}] {unit_text}"


def canonical_name_map(
    reagents_df: "pd.DataFrame",
) -> dict[str, tuple[str, str]]:
    """Build ``normalized_reagent_key → (canonical_reagent, canonical_unit)``
    from a reagents CSV DataFrame.

    - **Reagent name** comes from the optional ``reagent_canonical_name``
      column when present, falling back to the ``reagent`` column when
      that entry is blank or the column is missing entirely.
    - **Unit** comes from the ``units`` column when present; otherwise
      an empty string. Used as the canonical unit-spelling so that
      conditions CSVs with mismatched unit casing (``mg/mL`` vs
      ``mg/ml``) collapse to one column after normalization.

    Reagents not in the CSV simply aren't in the returned map;
    callers fall back to the incoming reagent and unit names.
    """
    if "reagent" not in reagents_df.columns:
        return {}
    has_canonical = "reagent_canonical_name" in reagents_df.columns
    has_units = "units" in reagents_df.columns
    result: dict[str, tuple[str, str]] = {}
    for _, row in reagents_df.iterrows():
        reagent_value = row["reagent"]
        if pd.isna(reagent_value) or not str(reagent_value).strip():
            continue
        key = normalize_reagent_name(reagent_value)
        canonical_reagent = (
            row["reagent_canonical_name"] if has_canonical else None
        )
        if pd.isna(canonical_reagent) or not str(canonical_reagent).strip():
            canonical_reagent = reagent_value
        unit_value = row["units"] if has_units else None
        canonical_unit = (
            "" if pd.isna(unit_value) else str(unit_value).strip()
        )
        result[key] = (str(canonical_reagent).strip(), canonical_unit)
    return result


def normalize_column_name(
    column: str,
    canonical_map: dict[str, tuple[str, str]],
) -> str:
    """Rewrite a ``<reagent> <unit>`` column header into canonical form.

    Looks up the canonical reagent and unit via ``canonical_map``.
    Reagents not in the map keep their incoming name (with any
    wrapping ``[]``/``()`` peeled before bracketing — avoids
    double-bracketing inputs like ``[PMix]``). Units in the map win
    over the incoming unit's case, which makes ``mg/mL`` and
    ``mg/ml`` collapse to a single output column.

    Headers without an embedded unit are returned unchanged (no way
    to know if a single-token header is a reagent or metadata).
    """
    parts = split_concentration_column_name(column)
    if parts is None:
        return column
    reagent, unit = parts
    bare_reagent = strip_wrapping_pairs(reagent)
    bare_unit = strip_wrapping_pairs(unit)
    canonical = canonical_map.get(normalize_reagent_name(bare_reagent))
    if canonical is None:
        return format_bracketed_column_name(bare_reagent, bare_unit)
    canonical_reagent, canonical_unit = canonical
    return format_bracketed_column_name(
        canonical_reagent, canonical_unit or bare_unit
    )
