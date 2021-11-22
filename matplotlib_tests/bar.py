import os
import typing

import numpy as np
import matplotlib.pyplot as plt

from file_helper import create_plot_dir


# MARK: - Directories
BAR_ROOT_DIR: typing.Final = "out/bar"


# MARK: - Bar
def test_bar():
    """
    Source: https://stackoverflow.com/questions/33497559/display-a-histogram-with-very-non-uniform-bin-widths
    """
    uniform_distribution = np.random.uniform(0.0, 1.5, (210000,))
    bin_edges = [0.0, 0.1, 0.3, 0.7, 1.5]    # Ranges: 0.1, 0.2, 0.4, 0.8

    hist, bin_edges = np.histogram(uniform_distribution, bin_edges)    # I think `bin_edges` is unchanged here.
    plt.bar(range(len(hist)), hist, width=1, align="center", tick_label=[f"{bin_edges[i]} - {bin_edges[i + 1]}" for i, _ in enumerate(hist)])
    plt.savefig(os.path.join(BAR_ROOT_DIR, "uniform.png"))
    plt.clf()


# MARK: - Main
if __name__ == "__main__":
    # MARK: Switch to current dir
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print(f"Working directory: {os.getcwd()}")

    create_plot_dir(BAR_ROOT_DIR)

    test_bar()
