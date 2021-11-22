"""
Source: https://matplotlib.org/stable/tutorials/introductory/usage.html#the-object-oriented-interface-and-the-pyplot-interface

2 ways to use matplotlib:

1. Explicitly create figures and axes, and call methods on them (the "object-oriented (OO) style")
2. Rely on pyplot to automatically create and manage the figures and axes, and use pyplot functions for plotting

Generally: Use 1 for non-interactive plotting, and 2 for interactive plotting (e.g. Jupyter).

My opinion: 2 is there to mimic MATLAB. Just use 1 as a programmer.
"""

import os
import typing

import numpy as np
import matplotlib.pyplot as plt

from file_helper import create_plot_dir


PLOT_ROOT_DIR: typing.Final = "out/object_oriented_and_pyplot_interfaces"


def test_object_oriented():
    # Create sample data.
    x = np.linspace(0, 2, 1000)    # NOTE: Output `dtype` is never integer unless explicitly specified.
    # print(xs.dtype)    # float64

    # Create a figure containing a single axes.
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()

    # Plot data on the axes.
    ax.plot(x, x, label="$y = x$")
    ax.plot(x, x ** 2, label="$y = x^2$")
    ax.plot(x, x ** 3, label="$y = x^3$")
    # Matplotlib can parse TeX expressions enclosed in `$` pairs.
    # For convenience, use raw strings (r"") to treat backslashes as literal characters.

    # Add x and y labels to the axes.
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    # Add title.
    ax.set_title("Object-Oriented")

    # Take data labels from the artists, and convert them into a legend.
    ax.legend()

    fig.savefig(os.path.join(PLOT_ROOT_DIR, "object_oriented.svg"))


def test_pyplot():
    # It seems that `pyplot` just re-uses the current figure without creating a new one.
    # plt.clf()    # Clear current figure.
    plt.figure()    # Create a new figure.

    # Create sample data.
    x = np.linspace(0, 2, 1000)

    # Plot data on the implicitly created axes.
    plt.plot(x, x, label="$y = x$")
    plt.plot(x, x ** 2, label="$y = x^2$")
    plt.plot(x, x ** 3, label="$y = x^3$")

    # Add x and y labels to the implicitly created axes.
    plt.xlabel("x")
    plt.ylabel("y")

    # Add title.
    plt.title("pyplot")

    # Take data labels from the artists, and convert them into a legend.
    plt.legend()

    plt.savefig(os.path.join(PLOT_ROOT_DIR, "pyplot.svg"))


# MARK: - Main
if __name__ == "__main__":
    # Switch to current dir.
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print(f"Working directory: {os.getcwd()}")

    create_plot_dir(PLOT_ROOT_DIR)

    test_object_oriented()
    test_pyplot()
