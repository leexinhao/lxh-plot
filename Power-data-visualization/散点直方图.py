# -*- coding: utf-8 -*-
"""
散点图加轴两边直方图
需要调整子图位置详见
https://matplotlib.org/gallery/lines_bars_and_markers/scatter_hist.html#sphx-glr-gallery-lines-bars-and-markers-scatter-hist-py
@author: lxh
"""
import numpy as np
import matplotlib.pyplot as plt


def draw_scatter_hist(x, y, c=None, xlabel=None, ylabel=None,
title=None, filepath=None, format='svg'):
        
    with plt.style.context('science'):
        # definitions for the axes
        left, width = 0.1, 0.65
        bottom, height = 0.1, 0.65
        spacing = 0.005

        rect_scatter = [left, bottom, width, height]
        rect_histx = [left, bottom + height + spacing, width, 0.2]
        rect_histy = [left + width + spacing, bottom, 0.2, height]

        # start with a square Figure
        fig = plt.figure(figsize=(8, 8))

        ax = fig.add_axes(rect_scatter)
        ax_histx = fig.add_axes(rect_histx, sharex=ax)
        ax_histy = fig.add_axes(rect_histy, sharey=ax)

        # no labels
        ax_histx.tick_params(axis="x", labelbottom=False)
        ax_histy.tick_params(axis="y", labelleft=False)

        # the scatter plot:
        N = len(x)
        if c == None:
            area = (20 * np.random.rand(N))**2  # 0 to 10 point radii
            c = np.sqrt(area)
        ax.scatter(x, y, c=c)
        # now determine nice limits by hand:
        binwidth = 0.25
        xymax = max(np.max(np.abs(x)), np.max(np.abs(y)))
        lim = (int(xymax/binwidth) + 1) * binwidth

        bins = np.arange(-lim, lim + binwidth, binwidth)
        ax_histx.hist(x, bins=bins, color='#2CB17E')
        ax_histy.hist(y, bins=bins, orientation='horizontal', color='#2B758E')
        
        if xlabel != None:
            ax.set_xlabel(xlabel)
        if ylabel != None:
            ax.set_ylabel(ylabel)
        if title != None:
            ax.set_title(title)

        if filepath != None:
            plt.savefig(filepath, format=format)
        plt.show()

if __name__ == '__main__':

    # some random data
    x = np.random.randn(1000)
    y = np.random.randn(1000)
    draw_scatter_hist(x, y, xlabel='x', ylabel='y', title='title')
