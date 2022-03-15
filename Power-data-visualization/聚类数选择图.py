# -*- coding: utf-8 -*-
"""
选择聚类数时画的图
@author: lxh
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import copy




def draw_choose_K(x, silhouette_scores, calinski_harabasz_scores,
                  davies_bouldin_scores, inertias=None, title=None, filepath=None, formats=None):
    r'''
    inertias属于可选项
    '''
    plt.rcParams['font.family'] = ['Times New Roman']
    plt.figure(figsize=(8, 6))
    if np.any(inertias) != None:
        inertias = np.array(inertias)
    silhouette_scores = np.array(silhouette_scores)
    calinski_harabasz_scores = np.array(calinski_harabasz_scores)
    davies_bouldin_scores = np.array(davies_bouldin_scores)
    # 归一化方便作图
    if np.any(inertias) != None:
        inertias -= inertias.min()
        inertias /= (inertias.max() - inertias.min())
    silhouette_scores -= silhouette_scores.min()
    silhouette_scores /= (silhouette_scores.max() - silhouette_scores.min())
    calinski_harabasz_scores -= calinski_harabasz_scores.min()
    calinski_harabasz_scores /= (calinski_harabasz_scores.max() -
                                calinski_harabasz_scores.min())
    davies_bouldin_scores -= davies_bouldin_scores.min()
    davies_bouldin_scores /= (davies_bouldin_scores.max() -
                            davies_bouldin_scores.min())

    plt.grid(linestyle="--")  # 设置背景网格线为虚线
    ax = plt.gca()


    if np.any(inertias) != None:
        plt.plot(x, inertias, marker='o', color="blue",
                label="inertia", linewidth=1.5)
    plt.plot(x, silhouette_scores, marker='o', color="green",
            label="SI", linewidth=1.5)
    plt.plot(x, calinski_harabasz_scores, marker='o', color="red",
            label="CH", linewidth=1.5)
    plt.plot(x, davies_bouldin_scores, marker='o', color="yellow",
            label='DB', linewidth=1.5)

    group_labels = x  # x轴刻度的标识
    plt.xticks(x, group_labels, fontsize=12, fontweight='bold')  # 默认字体大小为10
    plt.yticks(fontsize=12, fontweight='bold')
    if title != None:
        plt.title(title, fontsize=12, fontweight='bold')  # 默认字体大小为12
    plt.xlabel("Number of clusters", fontsize=13, fontweight='bold')
    plt.ylabel("CVI scores", fontsize=13, fontweight='bold')
    plt.xlim(1, len(x)+2)  # 设置x轴的范围
    plt.ylim(0, 1)
    # 显示各曲线的图例
    plt.legend(loc=0, numpoints=1)
    leg = plt.gca().get_legend()
    ltext = leg.get_texts()
    plt.setp(ltext, fontsize=12, fontweight='bold')  # 设置图例字体的大小和粗细

    if filepath is not None and formats is not None:
        for format in formats:
            plt.savefig(filepath+'.'+format, format=format)
    plt.show()


if __name__ == '__main__':

    # 测试draw_choose_K
    x = np.arange(2, 13)
    inertias = np.random.random(x.shape)
    silhouette_scores = np.random.random(x.shape)
    calinski_harabasz_scores = np.random.random(x.shape)
    davies_bouldin_scores = np.random.random(x.shape)
    draw_choose_K(x, silhouette_scores, calinski_harabasz_scores,
                  davies_bouldin_scores, filepath=None)
