# -*- coding: utf-8 -*-
"""
选择PCA降维数时画的图
@author: lxh
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import copy

'''
dim: 最大维度
x2: 0.9 0.95 0.99对应的维度
ch: 选择0.9 0.95 0.99其中之一，
'''


def draw_PCA(dim, x2, explained_variance_ratio: list, ch=None, title=None, filepath=None, formats=None):
    plt.rcParams['font.family'] = ['Times New Roman']
    assert dim == len(explained_variance_ratio)
    x = np.arange(0, dim+1)
    explained_variance_ratio = [0] + explained_variance_ratio
    for i in range(1, len(explained_variance_ratio)):
        explained_variance_ratio[i] += explained_variance_ratio[i - 1]

    plt.figure(figsize=(8, 4))
    # plt.style.use(['science'])

    plt.grid(linestyle="--")  # 设置背景网格线为虚线
    ax = plt.gca()

    plt.plot(x, explained_variance_ratio, color="red", linewidth=1)

    y2 = []

    for i in x2:
        y2.append(explained_variance_ratio[i])
    if ch != None:
        plt.plot(x2[ch], y2[ch], 'd', color='red', markersize=8)
        x2.remove(x2[ch])
        y2.remove(y2[ch])
    plt.plot(x2, y2, 's', linewidth=2)

    if title != None:
        plt.title(title, fontsize=12)  # 默认字体大小为12
    plt.xlabel("Number of principal components",
               fontsize=13)
    plt.ylabel("Explained variance ratio", fontsize=13)
    plt.xlim(0, len(x)-1)  # 设置x轴的范围
    plt.ylim(0, 1)

    # 建议保存为svg格式,再用inkscape转为矢量图emf后插入word中
    if filepath is not None and formats is not None:
        for format in formats:
            plt.savefig(filepath+'.'+format, format=format)
    plt.show()

if __name__ == '__main__':

    # 测试draw_PCA
    explained_variance_ratio = [0.4, 0.3, 0.12, 0.1, 0.05, 0.03]
    draw_PCA(6, [3, 4, 5], explained_variance_ratio, ch=1, filepath=None)
