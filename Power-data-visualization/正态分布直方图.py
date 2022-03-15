# -*- coding: utf-8 -*-
"""
直方图加正态分布曲线拟合
@author: lxh
"""

import matplotlib
import numpy as np
import matplotlib.pyplot as plt

def draw_hist_normal(x, mu=0, sigma=1, xlabel=None, ylabel=None,
                     title=None, filepath=None, format='svg'):
    with plt.style.context('science'):
        num_bins = len(x) // 10
        plt.figure(figsize=(6, 5))
        # the histogram of the data
        n, bins, patches = plt.hist(
            x, num_bins, density=True, color='#87CEEB')

        # add a 'best fit' line
        y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
             np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
        plt.plot(bins, y, '--', color='#FFD700', linewidth=1.5)
        if xlabel != None:
            plt.xlabel(xlabel)
        if ylabel != None:
            plt.ylabel(ylabel)
        if title != None:
            plt.title(title)

        # Tweak spacing to prevent clipping of ylabel
        plt.tight_layout()

        if filepath != None:
            plt.savefig(filepath, format=format)
        plt.show()


if __name__ == '__main__':
    np.random.seed(19680801)

    # example data
    mu = 100  # mean of distribution
    sigma = 15  # standard deviation of distribution
    x = mu + sigma * np.random.randn(437)
    xlabel = 'Smarts'
    ylabel = 'Probability density'
    title = r'Histogram of IQ: $\mu=100$, $\sigma=15$'
    draw_hist_normal(x, mu=mu, sigma=sigma, xlabel=xlabel,
                     ylabel=ylabel, title=title)
