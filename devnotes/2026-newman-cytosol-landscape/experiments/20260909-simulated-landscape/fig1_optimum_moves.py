#!/usr/bin/env python3
"""Figure 1 for the "What is a PURE landscape?" post.

Steady-state yield against magnesium, before and after adding Protein X.
At the magnesium you originally picked, the new system looks worse. Move along
the magnesium axis and most of the yield is still there — the optimum moved, it
did not disappear.

The curves are illustrative Gaussians, not fitted data. Ranges and amplitudes are
set to sit inside what our own sweeps actually cover (Mg 0-24 mM, yields up to
~50 ng/uL) so the picture doesn't imply a regime we've never run.

Usage
-----
    python3 fig1_optimum_moves.py                # single panel (the figure in the post)
    python3 fig1_optimum_moves.py --two-panel    # adds the Mg x Protein X view
    python3 fig1_optimum_moves.py --out other.png
"""

import argparse
from pathlib import Path

import matplotlib.patheffects as pe
import matplotlib.pyplot as plt
import numpy as np

# --- what the picture says -------------------------------------------------
# Tune these; every annotation below is computed from them, so the labels stay
# correct if you move a peak.
BASELINE = dict(mu=9.0, sigma=3.4, amp=50.0)   # mM, mM, ng/uL
WITH_X   = dict(mu=13.0, sigma=3.8, amp=41.0)
MG_RANGE = (0.0, 24.0)

# Protein X level that the "+ Protein X" curve corresponds to, and how far up the
# surface panel keeps going. Deliberately PX_SLICE < PX_MAX so the slice we are
# discussing sits inside the plot instead of on the top spine -- you can see that
# the ridge carries on past it.
PX_SLICE = 0.60
PX_MAX = 1.0

C_BASE = "#2a78d6"   # blue
C_NEW  = "#eb6834"   # orange   (blue/orange survives every common CVD type)
C_INK  = "#1a1a1a"
C_SUB  = "#5c5c5c"


def gaussian(x, mu, sigma, amp):
    """Illustrative response curve: one optimum, symmetric falloff."""
    return amp * np.exp(-((x - mu) ** 2) / (2.0 * sigma**2))


def _style(ax):
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color("#b9b9b9")
    ax.tick_params(colors=C_SUB, labelsize=9.5, length=4)
    for lbl in ax.get_xticklabels() + ax.get_yticklabels():
        lbl.set_color(C_SUB)


def panel_sweep(ax, show_level=False):
    """The 1-D view: what you actually see when you sweep magnesium."""
    mg = np.linspace(*MG_RANGE, 600)
    y_base = gaussian(mg, **BASELINE)
    y_new = gaussian(mg, **WITH_X)

    mg_old = BASELINE["mu"]                       # the magnesium you settled on
    mg_new = WITH_X["mu"]                         # where the optimum went
    y_at_old = gaussian(mg_old, **WITH_X)         # what you measure if you don't re-optimise
    y_at_new = WITH_X["amp"]
    y_peak_base = BASELINE["amp"]

    drop_pct = 100 * (1 - y_at_old / y_peak_base)
    recovered_pct = 100 * y_at_new / y_peak_base

    ax.plot(mg, y_base, color=C_BASE, lw=2.2, label="baseline cytosol", zorder=3)
    new_label = f"+ Protein X ({PX_SLICE:g} a.u.)" if show_level else "+ Protein X"
    ax.plot(mg, y_new, color=C_NEW, lw=2.2, label=new_label, zorder=3)

    # the magnesium you had already chosen
    ax.axvline(mg_old, color="#9a9a9a", lw=1.0, ls=(0, (3, 4)), zorder=1)
    ax.annotate(
        "the Mg you picked\nfrom the baseline sweep",
        xy=(mg_old, -0.055), xycoords=("data", "axes fraction"),
        ha="center", va="top", fontsize=8.5, color=C_SUB, linespacing=1.4,
        annotation_clip=False,
    )

    ax.scatter([mg_old], [y_peak_base], s=46, color=C_BASE, zorder=5,
               edgecolor="white", linewidth=1.2)
    ax.scatter([mg_old], [y_at_old], s=46, color=C_NEW, zorder=5,
               edgecolor="white", linewidth=1.2)
    ax.scatter([mg_new], [y_at_new], s=46, color=C_NEW, zorder=5,
               edgecolor="white", linewidth=1.2)

    # the apparent loss, measured where you were standing
    ax.annotate(
        "", xy=(mg_old, y_peak_base), xytext=(mg_old, y_at_old),
        arrowprops=dict(arrowstyle="<->", color=C_SUB, lw=1.1, shrinkA=3, shrinkB=3),
        zorder=4,
    )
    ax.annotate(
        f"looks like a {drop_pct:.0f}% loss",
        xy=(mg_old - 0.5, (y_peak_base + y_at_old) / 2),
        ha="right", va="center", fontsize=9, color=C_INK,
        bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.85),
    )

    # ...but the peak just moved. Kept low and straight so it reads as
    # "step along the x axis" instead of tangling with the curve itself.
    y_shift = y_peak_base * 0.09
    ax.annotate(
        "", xy=(mg_new, y_shift), xytext=(mg_old, y_shift),
        arrowprops=dict(arrowstyle="-|>", color=C_NEW, lw=1.5, shrinkA=0, shrinkB=0),
        zorder=4,
    )
    ax.annotate(
        f"move +{mg_new - mg_old:.0f} mM Mg",
        xy=((mg_old + mg_new) / 2, y_shift * 1.35), ha="center", va="bottom",
        fontsize=9, color=C_NEW,
    )
    ax.annotate(
        f"…and you're back to\n{recovered_pct:.0f}% of baseline",
        xy=(mg_new, y_at_new), xytext=(mg_new + 3.0, y_at_new + y_peak_base * 0.16),
        ha="left", va="bottom", fontsize=9, color=C_NEW, linespacing=1.4,
        arrowprops=dict(arrowstyle="-", color=C_NEW, lw=1.0, alpha=0.7,
                        shrinkA=2, shrinkB=6),
    )

    ax.set_xlabel("[Mg$^{2+}$]  (mM)", fontsize=10.5, color=C_INK, labelpad=26)
    ax.set_ylabel("steady-state yield", fontsize=10.5, color=C_INK)
    ax.set_xlim(*MG_RANGE)
    ax.set_ylim(0, y_peak_base * 1.28)
    ax.legend(frameon=False, fontsize=9.5, loc="upper right",
              labelcolor=C_INK, handlelength=1.8)
    _style(ax)


def _slice_line(ax, y, color, label):
    """A horizontal cut through the surface, with a white halo so the colour
    survives whatever the colormap is doing underneath it."""
    halo = [pe.withStroke(linewidth=3.6, foreground="white")]
    ax.axhline(y, color=color, lw=1.8, ls=(0, (5, 3)), zorder=4, path_effects=halo)
    ax.annotate(
        label, xy=(MG_RANGE[1] * 0.975, y + 0.022), ha="right", va="bottom",
        fontsize=8.5, color=C_INK, zorder=6,
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="none", alpha=0.88),
    )


def panel_surface(ax):
    """The 2-D view: the ridge bends, and both curves on the left are cuts across it."""
    mg = np.linspace(*MG_RANGE, 260)
    px = np.linspace(0.0, PX_MAX, 260)       # Protein X, arbitrary units
    MG, PX = np.meshgrid(mg, px)

    # Interpolate in units of PX_SLICE, so the surface reproduces WITH_X exactly at
    # PX_SLICE and keeps going above it. The two panels then cannot disagree.
    t = PX / PX_SLICE
    mu = BASELINE["mu"] + (WITH_X["mu"] - BASELINE["mu"]) * t
    sigma = BASELINE["sigma"] + (WITH_X["sigma"] - BASELINE["sigma"]) * t
    amp = BASELINE["amp"] + (WITH_X["amp"] - BASELINE["amp"]) * t
    Z = amp * np.exp(-((MG - mu) ** 2) / (2.0 * sigma**2))

    cf = ax.contourf(MG, PX, Z, levels=14, cmap="viridis")
    cb = ax.figure.colorbar(cf, ax=ax, pad=0.02)
    cb.set_label("steady-state yield", fontsize=9.5, color=C_SUB)
    cb.ax.tick_params(colors=C_SUB, labelsize=8.5)
    cb.outline.set_visible(False)

    # where the optimum sits at each level of Protein X
    ridge = BASELINE["mu"] + (WITH_X["mu"] - BASELINE["mu"]) * (px / PX_SLICE)
    ax.plot(ridge, px, color="white", lw=1.6, ls=(0, (4, 3)), zorder=3,
            path_effects=[pe.withStroke(linewidth=3.4, foreground="#1a1a1a", alpha=0.35)])
    ax.annotate(
        "the optimum,\nas it moves",
        xy=(ridge[-6], PX_MAX * 0.94), xytext=(ridge[-6] - 2.4, PX_MAX * 0.86),
        ha="right", va="center", fontsize=8.5, color=C_INK, zorder=6, linespacing=1.4,
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="none", alpha=0.88),
        arrowprops=dict(arrowstyle="-", color="white", lw=1.2, shrinkA=4, shrinkB=4),
    )

    # the two cuts that produced the curves on the left. The ridge already shows the
    # path between them, so the markers alone carry the "it moved" point.
    _slice_line(ax, 0.0, C_BASE, "baseline sweep — Protein X held at 0")
    _slice_line(ax, PX_SLICE, C_NEW, "the slice you're in now")

    ax.scatter([BASELINE["mu"]], [0.0], s=58, color=C_BASE, zorder=6,
               edgecolor="white", linewidth=1.4)
    ax.scatter([WITH_X["mu"]], [PX_SLICE], s=58, color=C_NEW, zorder=6,
               edgecolor="white", linewidth=1.4)

    ax.set_xlabel("[Mg$^{2+}$]  (mM)", fontsize=10.5, color=C_INK)
    ax.set_ylabel("[Protein X]  (a.u.; 0 = baseline cytosol)",
                  fontsize=10.5, color=C_INK)
    ax.set_xlim(*MG_RANGE)
    # a sliver of headroom below zero so the baseline cut sits clear of the spine
    ax.set_ylim(-0.035, PX_MAX)
    ax.set_yticks(np.arange(0, PX_MAX + 0.01, 0.2))
    _style(ax)


def make_figure(two_panel=False, surface_only=False):
    if surface_only:
        # Just the right-hand panel, for use as the DevNote thumbnail.
        fig, ax = plt.subplots(figsize=(6.4, 4.6))
        panel_surface(ax)
    elif two_panel:
        fig, axes = plt.subplots(1, 2, figsize=(12.4, 4.6))
        panel_sweep(axes[0], show_level=True)
        panel_surface(axes[1])
        axes[0].set_title("A single factor sweep shows one slice", fontsize=11,
                          color=C_INK, loc="left", pad=12)
        axes[1].set_title("Both curves are slices of the same surface", fontsize=11,
                          color=C_INK, loc="left", pad=12)
    else:
        fig, ax = plt.subplots(figsize=(7.2, 4.8))
        panel_sweep(ax)
    fig.tight_layout()
    return fig


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--two-panel", action="store_true",
                    help="add the Mg x Protein X surface alongside the sweep")
    ap.add_argument("--surface-only", action="store_true",
                    help="render only the Mg x Protein X surface, for the thumbnail")
    ap.add_argument("--out", default=None, help="output path (.png; .svg also written)")
    args = ap.parse_args()

    if args.surface_only:
        # the DevNote thumbnail lives in assets/, two levels up from this script
        out = Path(args.out or Path(__file__).parents[2] / "assets" / "thumbnail.png")
    else:
        default = "fig1-optimum-moves-2panel.png" if args.two_panel else "fig1-optimum-moves.png"
        out = Path(args.out or Path(__file__).parent / default)

    fig = make_figure(two_panel=args.two_panel, surface_only=args.surface_only)
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, dpi=220, bbox_inches="tight", facecolor="white")
    if args.surface_only:
        # no companion svg: assets/ holds the raster thumbnail only
        print(f"wrote {out}")
    else:
        fig.savefig(out.with_suffix(".svg"), bbox_inches="tight", facecolor="white")
        print(f"wrote {out} and {out.with_suffix('.svg')}")
