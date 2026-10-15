"""Render the homepage's mathematical accent (requires matplotlib, numpy, Pillow)."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection
from matplotlib.colors import LinearSegmentedColormap
from PIL import Image


OUTPUT = Path(__file__).resolve().parents[1] / "assets/media/math-banner.webp"


def main():
    x, y = np.meshgrid(np.linspace(-11, 11, 133), np.linspace(-9, 9, 109))
    envelope = np.exp(-(x**2 + y**2) / 28)
    z = envelope * np.sin(x) * np.cos(y)

    # Orthographic view of the supplied surface, with vertical relief emphasized.
    azimuth, elevation = np.deg2rad([40, 29])
    u = np.cos(azimuth) * x - np.sin(azimuth) * y
    v = -np.sin(elevation) * (np.sin(azimuth) * x + np.cos(azimuth) * y)
    v += np.cos(elevation) * z * 3
    points = np.stack((u, v), axis=-1)

    segments = np.concatenate(
        [
            np.stack((points[:, :-1], points[:, 1:]), axis=2).reshape(-1, 2, 2),
            np.stack((points[:-1], points[1:]), axis=2).reshape(-1, 2, 2),
        ]
    )
    heights = np.concatenate(
        [((z[:, :-1] + z[:, 1:]) / 2).ravel(), ((z[:-1] + z[1:]) / 2).ravel()]
    )
    strength = np.concatenate(
        [
            ((envelope[:, :-1] + envelope[:, 1:]) / 2).ravel(),
            ((envelope[:-1] + envelope[1:]) / 2).ravel(),
        ]
    )
    # Fade the original grid coordinates, not the projected screen coordinates.
    distance = np.sqrt(x**2 + y**2)
    radius = np.concatenate(
        [((distance[:, :-1] + distance[:, 1:]) / 2).ravel(),
         ((distance[:-1] + distance[1:]) / 2).ravel()]
    )
    fade = np.clip((radius - 5.0) / 4.0, 0, 1)
    edge = 1 - fade**2 * (3 - 2 * fade)
    palette = LinearSegmentedColormap.from_list("research", ["#308de5", "#a449cc"])
    colors = palette(np.clip((heights + 0.93) / 1.86, 0, 1))
    colors[:, 3] = (0.08 + 0.58 * strength) * edge

    fig = plt.figure(figsize=(16, 3.8), dpi=200)
    ax = fig.add_axes((0, 0, 1, 1))
    ax.add_collection(LineCollection(segments, colors=colors, linewidths=0.5))
    ax.set_xlim(-9.8, 9.8)
    ax.set_ylim(-5.4, 5.4)
    ax.set_axis_off()
    fig.canvas.draw()

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray(np.asarray(fig.canvas.buffer_rgba())).convert("RGB").save(
        OUTPUT, "WEBP", quality=90, method=6
    )
    plt.close(fig)
    print(f"Rendered {OUTPUT}")


if __name__ == "__main__":
    main()
