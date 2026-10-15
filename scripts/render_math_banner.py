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
    x, y = np.meshgrid(np.linspace(-10, 10, 121), np.linspace(-8, 8, 97))
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
    fade = np.clip((radius - 4.5) / 3.5, 0, 1)
    edge = 1 - fade**2 * (3 - 2 * fade)
    palette = LinearSegmentedColormap.from_list("research", ["#328b91", "#4f7ca6", "#596ea0"])
    colors = palette(np.clip((heights + 0.93) / 1.86, 0, 1))
    colors[:, 3] = (0.06 + 0.48 * strength) * edge

    fig = plt.figure(figsize=(16, 3.8), dpi=200)
    ax = fig.add_axes((0, 0, 1, 1))
    ax.add_collection(LineCollection(segments, colors=colors, linewidths=0.5))
    ax.set_xlim(-10.5, 10.5)
    ax.set_ylim(-5.2, 5.2)
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
