import os

import numpy as np
import matplotlib.pyplot as plt


# MARK: - Histogram
# MARK: Auto x label ranges
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


# MARK: Log scale x label ranges
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


# MARK: Custom x label ranges (failed)
def test_custom_scale_histogram():
    """
    Doesn't work as expected.

    The longer the range, the wider the pillar in the image.

    Use `plt.bar` instead (see the `bar.test_bar` function).
    """
    uniform_distribution = np.random.uniform(0.0, 1.5, (210000,))

    bin_edges = [0.0, 0.1, 0.3, 0.7, 1.5]    # Ranges: 0.1, 0.2, 0.4, 0.8

    plt.hist(uniform_distribution, bins=bin_edges)
    plt.gca().set(title=f"Uniform Distribution, size: {np.size(uniform_distribution)}")
    plt.savefig("out/hist_custom_uniform.png")
    plt.clf()


# MARK: - Main
if (__name__ == "__main__"):
    # MARK: Switch to current dir
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print(f"Working directory: {os.getcwd()}")

    # test_histogram()
    # test_log_scale_histogram()
    test_custom_scale_histogram()
