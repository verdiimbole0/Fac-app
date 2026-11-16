# -*- coding: utf-8 -*-
"""Bibliothèque graphique commune : palette, boîtes, flèches, export PNG+SVG."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Ellipse, Rectangle, Polygon, Wedge

ROOT = Path(__file__).resolve().parents[1]
ILL = ROOT / "02_ILLUSTRATIONS"

NAVY, GOLD, GREY, TURQ, RED, INK = "#0B2545", "#C9A227", "#EEF1F5", "#13A89E", "#B23A48", "#222831"
LIGHTNAVY, LIGHTTURQ, LIGHTGOLD, LIGHTRED = "#DCE4EF", "#D5EFEC", "#F6EDCC", "#F5DDE1"
MID = "#5B6B7F"
ORANGE, PURPLE, GREEN = "#D9822B", "#6A4C93", "#2D6A4F"

plt.rcParams.update({
    "font.family": ["Inter", "DejaVu Sans"], "font.size": 10, "axes.edgecolor": MID,
    "axes.labelcolor": INK, "xtick.color": INK, "ytick.color": INK, "axes.titleweight": "bold",
    "axes.titlecolor": NAVY, "svg.fonttype": "none",
})

def canvas(w=10, h=5.6, xmax=100, ymax=56):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(0, xmax); ax.set_ylim(0, ymax); ax.axis("off")
    return fig, ax

def box(ax, x, y, w, h, text="", fc=LIGHTNAVY, ec=NAVY, fs=9.5, color=INK, bold=False, lw=1.4,
        rounding=1.6, ha="center", va="center", style="round", alpha=1.0, zorder=2):
    p = FancyBboxPatch((x, y), w, h, boxstyle=f"{style},pad=0,rounding_size={rounding}" if style == "round" else style,
                       fc=fc, ec=ec, lw=lw, alpha=alpha, zorder=zorder)
    ax.add_patch(p)
    if text:
        tx = x + w / 2 if ha == "center" else x + 1.2
        ax.text(tx, y + h / 2, text, ha=ha, va=va, fontsize=fs, color=color,
                fontweight="bold" if bold else "normal", zorder=zorder + 1, linespacing=1.25, wrap=False)
    return p

def arrow(ax, p1, p2, color=MID, lw=1.6, style="-|>", ms=14, ls="-", rad=0.0, zorder=1):
    a = FancyArrowPatch(p1, p2, arrowstyle=style, mutation_scale=ms, color=color, lw=lw, linestyle=ls,
                        connectionstyle=f"arc3,rad={rad}", zorder=zorder, shrinkA=2, shrinkB=2)
    ax.add_patch(a); return a

def title(ax, text, y=None, x=50, fs=13, color=NAVY):
    ax.text(x, y if y is not None else ax.get_ylim()[1] - 2.5, text, ha="center", va="center",
            fontsize=fs, fontweight="bold", color=color)

def note(ax, text, x=50, y=1.5, fs=7.5, color=MID, ha="center"):
    ax.text(x, y, text, ha=ha, va="center", fontsize=fs, color=color, style="italic")

def save(fig, name, sub="SCHEMAS"):
    d = ILL / sub; d.mkdir(parents=True, exist_ok=True)
    fig.savefig(d / f"{name}.png", dpi=200, bbox_inches="tight", facecolor="white")
    fig.savefig(d / f"{name}.svg", bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return d / f"{name}.png"

def style_axes(ax, grid=True):
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    if grid: ax.grid(axis="y", color="#D5DBE3", lw=0.6); ax.set_axisbelow(True)
