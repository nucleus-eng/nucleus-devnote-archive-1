A local, patched copy of the public Vizarr anywidget
(`https://curvenote.github.io/widgets/widgets/vizarr-viewer.js`), used to embed
[Vizarr](https://github.com/hms-dbmi/vizarr) — a client-side viewer for large,
multiscale OME-Zarr microscopy images — in a devnote's `main.md` via MyST's
native `{anywidget}` directive.

Pulled from `nucleus-eng/devstudio-board` at commit `54c823c`
(2026-10-11, "DevNote: pH sensor in solution (swh-20260925)"), which is where
the two fixes below were built and is kept canonical. Re-pull from there
rather than hand-editing a divergent copy here. The unpatched original is
kept beside this file as `vizarr-viewer.upstream.js` so the diff stays
visible.

## What this fixes

Vizarr's control panel is built with Material-UI, which injects its rules as
`<style>` tags in `document.head`. myst-theme mounts an anywidget inside a
shadow root. A style tag in the document does not cross that boundary. Every
slider renders at 0x0 without the rules, and even once sized, the panel
paints under deck.gl's canvas and cannot be dragged. This copy mirrors the
two sets of rules that matter (anything mentioning `Mui`, and anything
carrying `data-jss`, vizarr's own makeStyles output) into the shadow root. It
keeps mirroring as Material-UI injects more of them lazily.

It also lets a devnote set its own per-channel colors and contrast limits.
Vizarr ignores the `colors` and `contrast_limits` passed to `addImage`.
It reads them from a store's own `omero` metadata instead. This copy patches
`fetch` to rewrite that metadata on the way in, for any source a devnote
registers those values against.

Both fixes, and how they were diagnosed, are documented in full at the top of
`vizarr-viewer.mjs`.

## Using this in a devnote

Point the `{anywidget}` directive at this file directly, by relative path.
There is no separate plugin registration step, unlike `{seqviz}` and
`{platemap}`, because `{anywidget}` is a native MyST directive:

```
:::{anywidget} ../../plugins/vizarr/vizarr-viewer.mjs
:class: w-full

{
    "source": "https://your-zarr-source/...",
    "height": "600px",
    "menuOpen": true
}
:::
```

No per-devnote copy of this file is needed. Unlike `platemap-widget.mjs`,
mystmd resolves this path as the directive's own argument, relative to the
document that uses it, not relative to a plugin's hardcoded internal path.

## Updating

Pull fresh from `nucleus-eng/devstudio-board` rather than editing here. This
copy exists only because the fixes are specific to how myst-theme mounts an
anywidget, not to any one devnote.
