# -*- coding: utf-8 -*-
"""
画MLP曲线图
@author: lxh
"""

import pickle
import sys
import os
import numpy as np
import matplotlib.pyplot as plt


def draw_MLPs(x, MLPs, ymax=None, draw_center=False, cluster_center=None,
              title=None, filepath=None, formats=('svg')):
    r'''
    x: 曲线维度，为24x31,48x31,96x31等
    MLPs: MLP数组或ndarray
    cluster_center: 聚类中心曲线，对于KMeans聚类来说好像就是平均的
    默认会画一条平均值曲线
    '''
    # with plt.style.context('science'):
    plt.rcParams['font.family'] = ['Times New Roman']
    label_font = {
        # 'weight': 'bold',
        'size': 18,
        'family': 'Times New Roman'
    }
    if ymax == None:
        ymax = int(MLPs.max()) + 1
    plt.figure(figsize=(8, 6))
    MLPs = np.array(MLPs)
    x = np.array(x)
    assert len(x) == MLPs.shape[1]

    for MLP in MLPs:
        if draw_center:
            plt.plot(x, MLP, color='#C8C8FF', linewidth=0.5)
        else:
            plt.plot(x, MLP, linewidth=0.5)

    ax = plt.gca()
    if draw_center:
        if np.any(cluster_center) != None:
            plt.plot(x, cluster_center, color='r',
                     linewidth=0.6, label='Cluster Center')
            plt.plot(x, MLPs.mean(axis=0), color='#8B0000',
                     linewidth=0.6, label='Mean MLP')
        else:
            plt.plot(x, MLPs.mean(axis=0), color='#8B0000',
                     linewidth=0.6, label='Cluster Center')
        plt.legend(prop={'size': 15})

    # ax.spines['right'].set_color('none')
    # ax.spines['top'].set_color('none')

    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    plt.xlim((0, len(x)))
    plt.ylim((0, ymax))
    plt.xlabel('Day', fontdict=label_font)
    plt.ylabel('Power consumption (kWh)', fontdict=label_font)
    plt.tick_params(axis='x')
    plt.tick_params(axis='y')
    ynew_ticks = np.linspace(0, ymax, 10)
    xticks_labels = ['1', '3', '5', '7', '9', '11',
                     '13', '15', '17', '19', '21', '23',
                     '25', '27', '29', '31']
    plt.xticks(np.linspace(0, len(x), len(xticks_labels)),
               xticks_labels, fontsize=13)
    plt.yticks(ynew_ticks, fontsize=13)
    if title != None:
        plt.title(title, fontdict=label_font)
    if filepath != None:
        for format in formats:
            plt.savefig(filepath+'.'+format, format=format)
    plt.show()


if __name__ == '__main__':
    LEN = 24*31
    x = np.arange(0, LEN)
    y = np.random.normal(size=(50, LEN))
    # draw_MLPs(x, y)
    draw_MLPs(x, y, cluster_center=np.random.rand(LEN))
    # draw_MLPs(x, y,
    #                   cluster_center=np.random.rand(LEN), filepath='./负荷曲线图MLPs示例.svg')
