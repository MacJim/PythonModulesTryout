"""
Source:

- <https://matplotlib.org/stable/tutorials/introductory/usage.html#parts-of-a-figure>
- <https://matplotlib.org/stable/tutorials/introductory/pyplot.html>
"""

import os
import typing

import numpy as np
import matplotlib.pyplot as plt

from file_helper import create_plot_dir


OUT_DIR: typing.Final = "out/plot"


def test_default_x_values():
    y = np.arange(1, 7)

    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()

    # When given 1 argument, `plot` treats it as y values.
    # The default x values are `np.arange(len of y)`.
    ax.plot(y, label="$y = x + 1$")

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("$y = x + 1$")

    fig.savefig(os.path.join(OUT_DIR, "default_x_values.svg"))


def test_formatting():
    """
    Check `https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html` for format strings.

    IMO the best option is to combine a high-resolution line and some low-resolution scattered markers.
    I don't think "markers connected by lines" is that useful.
    """
    # Sample data.
    high_res_x = np.linspace(0, 3, 1000)
    x = np.linspace(0, 3, 10)
    # print(x.dtype)    # float64

    # Create a figure containing a single axes.
    fig: plt.Figure
    fig, axs = plt.subplots(3, 1)    # `axs` is an `ndarray`.
    # fig.set_figwidth(fig.get_figwidth() * 2)
    fig.set_figheight(fig.get_figheight() * 3)

    line_ax: plt.Axes = axs[0]
    marker_ax: plt.Axes = axs[1]
    marker_connected_by_lines_ax: plt.Axes = axs[2]

    # MARK: Line formatting
    # Color is optional. I'm just specifying the styles here.
    line_ax.plot(high_res_x, high_res_x, label="b- (solid blue line, default)")
    line_ax.plot(high_res_x, high_res_x ** 2, "--", label="-- (dashed line)")
    line_ax.plot(high_res_x, high_res_x ** 3, "-.", label="-. (dash-dot line style)")
    line_ax.plot(high_res_x, high_res_x ** 4, ":", label=": (dotted line style)")

    line_ax.legend()
    line_ax.set_title("Line Formatting")

    # MARK: Marker formatting
    marker_ax.plot(x, x, ".", label=". (point marker)")
    marker_ax.plot(x, x ** 2, "o", label="o (circle marker)")
    marker_ax.plot(x, x ** 3, "v", label="v (triangle_down marker)")
    marker_ax.plot(x, x ** 4, "s", label="s (square marker)")

    marker_ax.legend()
    marker_ax.set_title("Marker Formatting")

    # MARK: Markers connected by lines
    marker_connected_by_lines_ax.plot(x, x, "-,", label="-,")
    marker_connected_by_lines_ax.plot(x, x ** 2, "--^", label="--^")
    marker_connected_by_lines_ax.plot(x, x ** 3, "-.*", label="-.*")
    marker_connected_by_lines_ax.plot(x, x ** 4, ":d", label=":d")

    marker_connected_by_lines_ax.legend()
    marker_connected_by_lines_ax.set_title("Markers Connected by Lines Formatting")

    fig.savefig(os.path.join(OUT_DIR, "formatting.svg"))


def test_tick_interval():
    pass


# MARK: - Main
if __name__ == "__main__":
    # Switch to current dir.
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print(f"Working directory: {os.getcwd()}")

    create_plot_dir(OUT_DIR)

    # test_default_x_values()
    test_formatting()
