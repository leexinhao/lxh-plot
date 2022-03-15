# -*- coding: utf-8 -*-
"""
选择聚类数时画的图
@author: lxh
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import copy


def draw_choose_K_alone(x, scores, choice=None, ylabel="CVI scores", title=None, filepath=None, formats=None):
    '''
    只画一个指标
    '''
    plt.rcParams['font.family'] = ['Times New Roman']
    plt.figure(figsize=(6, 4))

    plt.grid(linestyle="--")  # 设置背景网格线为虚线
    ax = plt.gca()

    
    if choice is not None:
        plt.plot(x, scores, color="#0462b2", linewidth=1.5)
        for i in range(len(x)):
            if i == choice:
                plt.plot(x[choice], scores[choice], marker='d',
                        color='#ec1f24', markersize=11)
            else:
                plt.plot(x[i], scores[i], marker='s',
                         color="#0462b2", markersize=8)
    else:
        plt.plot(x, scores, marker='s', color="#0462b2", linewidth=1.5, markersize=8)
    group_labels = x  # x轴刻度的标识
    plt.xticks(x, group_labels, fontsize=15, fontweight='bold')  # 默认字体大小为10
    plt.yticks(fontsize=15, fontweight='bold')
    if title != None:
        plt.title(title, fontsize=15, fontweight='bold')  # 默认字体大小为12
    plt.xlabel("Number of clusters", fontsize=15, fontweight='bold')
    plt.ylabel(ylabel, fontsize=15, fontweight='bold')
    plt.xlim(1, len(x)+2)  # 设置x轴的范围

    if filepath is not None and formats is not None:
        for format in formats:
            plt.savefig(filepath+'.'+format, format=format)
    plt.show()


if __name__ == '__main__':

    # 测试draw_choose_K
    x = np.arange(2, 13)
    silhouette_scores = np.random.random(x.shape)
    draw_choose_K_alone(x, silhouette_scores, choice=2)
