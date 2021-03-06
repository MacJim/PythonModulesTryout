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


def test_log_scale_histogram():
    # TODO:
    pass


# MARK: - Main
if (__name__ == "__main__"):
    # MARK: Switch to current dir
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print(f"Working directory: {os.getcwd()}")

    test_histogram()
