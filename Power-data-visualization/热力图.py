# -*- coding: utf-8 -*-
"""
画热力图，一般用于可视化聚类结果
@author: lxh
"""
import matplotlib.pyplot as plt
import numpy as np
import copy

def draw_heatmap(datas, title=None, xlabel=None,
 ylabel=None, xtick=None, ytick=None,
 filepath=None, format='svg'):
    with plt.style.context('science'):
        fig = plt.figure(figsize=(8, 4))
        ax = fig.gca()
        pcm = ax.pcolormesh(datas)
        fig.colorbar(pcm, ax=ax)
        if xlabel != None:
            plt.xlabel(xlabel)
        if ylabel != None:
            plt.ylabel(ylabel)
        if title != None:
            plt.title(title)
        if filepath != None:
            plt.savefig(filepath, format=format)
        plt.show()

if __name__ == '__main__':
    # 测试draw_heatmap
    datas = np.random.random((8760, 1))
    datas = copy.deepcopy(datas[0:8736])
    datas = datas.reshape((52, 24*7))
    draw_heatmap(datas, title='title',
    xlabel='xlabel', ylabel='ylabel')
