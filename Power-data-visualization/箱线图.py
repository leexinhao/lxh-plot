# -*- coding: utf-8 -*-
"""
箱线图
@author: lxh
"""
import matplotlib.pyplot as plt
import numpy as np


def draw_box(all_data, labels, notch=True,
xlabel=None, ylabel=None, title=None, filepath=None, format='svg'):
    with plt.style.context('science'):
        fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(9, 4))

        # box plot
        bplot = ax.boxplot(all_data,
                            notch=notch,  # notch shape
                            vert=True,  # vertical box alignment
                            patch_artist=True,  # fill with color
                            labels=labels)  # will be used to label x-ticks
        ax.set_title('Rectangular box plot')


        # fill with colors
        colors = ['pink', 'lightblue', 'lightgreen']

        for patch, color in zip(bplot['boxes'], colors):
            patch.set_facecolor(color)

        # adding horizontal grid lines

        ax.yaxis.grid(True)
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
    # Random test data
    np.random.seed(19680801)
    all_data = [np.random.normal(0, std, size=100) for std in range(1, 4)]
    labels = ['x1', 'x2', 'x3']
    xlabel = 'Three separate samples'
    ylabel = 'Observed values'
    draw_box(all_data, labels, xlabel=xlabel, ylabel=ylabel)
