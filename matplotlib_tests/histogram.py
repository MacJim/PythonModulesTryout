import os

import numpy as np
import matplotlib.pyplot as plt
from numpy.core.defchararray import title


# MARK: - Histogram
def test_histogram():
    normal_distribution = np.random.normal(0, 1, (210000,))
    """
    Mean 0, standard deviation 1.

    Shape: (1000,)
    """
    uniform_distribution = np.random.uniform(-1., 1., (210000,))

    bins_count = 100

    plt.figure(figsize=(9.0, 8.0))    # width, height

    plt.hist(normal_distribution, bins=bins_count)
    plt.gca().set(title=f"Normal Distribution, size: {np.size(normal_distribution)}")
    plt.savefig("out/hist_normal.png")
    plt.clf()    # Clear the current figure.

    plt.hist(uniform_distribution, bins=bins_count)
    plt.gca().set(title=f"Uniform Distribution, size: {np.size(uniform_distribution)}")
    plt.savefig("out/hist_uniform.png")
    plt.clf()


def _plot_log_histogram(x: np.ndarray, bins_count: int, plot_save_filename: str):
    """
    Source: https://stackoverflow.com/questions/47850202/plotting-a-histogram-on-a-log-scale-with-matplotlib
    """
    _, bins, _ = plt.hist(x, bins_count)
    log_bins = np.logspace(np.log10(bins[0]), np.log10(bins[-1]), len(bins))
    plt.clf()
    plt.hist(x, bins=log_bins)
    plt.xscale("log")
    plt.savefig(plot_save_filename)


def test_log_scale_histogram():
    uniform_distribution = np.random.uniform(1., 100., (210000,))
    log_uniform_distribution = np.log10(uniform_distribution)

    bins_count = 100

    _plot_log_histogram(log_uniform_distribution, bins_count, "out/hist_log_uniform.png")


# MARK: - Main
if (__name__ == "__main__"):
    # MARK: Switch to current dir
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print(f"Working directory: {os.getcwd()}")

    # test_histogram()
    test_log_scale_histogram()
