# -*- coding: utf-8 -*-
"""
画SLP曲线图
@author: lxh
"""

import pickle
import sys
import os
import numpy as np
import matplotlib.pyplot as plt

'''
x: 曲线维度，为24x91,48x7,96x7等
SLPs: SLP数组或ndarray
cluster_center: 聚类中心曲线，对于KMeans聚类来说好像就是平均的
默认会画一条平均值曲线
'''


def draw_SLPs(x, SLPs, season=None, ymax=None, cluster_center=None,
              title=None, filepath=None, format='svg'):
    with plt.style.context('science'):
        if ymax == None:
            ymax = int(SLPs.max()) + 1
        plt.figure(figsize=(8, 4))
        SLPs = np.array(SLPs)
        x = np.array(x)
        assert len(x) == SLPs.shape[1]

        for SLP in SLPs:
            plt.plot(x, SLP, color='#E6E6FA', linewidth=0.5)

        if np.any(cluster_center) != None:
            plt.plot(x, cluster_center, color='r',
                     linewidth=0.6, label='Cluster Center')
            plt.plot(x, SLPs.mean(axis=0), color='#8B0000',
                     linewidth=0.6, label='Mean SLP')
        else:
            plt.plot(x, SLPs.mean(axis=0), color='#8B0000',
                     linewidth=0.6, label='Cluster Center')
        ax = plt.gca()

        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')

        plt.legend()
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')

        plt.xlim((0, len(x)))
        plt.ylim((0, ymax))
        plt.ylabel('Power consumption (kWh)')
        plt.tick_params(axis='x')
        plt.tick_params(axis='y')
        ynew_ticks = np.linspace(0, ymax, 10)
        if season == None:
            xticks_labels = ['Month 1', 'Month 2', 'Month 3']
        elif season == 'Spr':
            xticks_labels = ['Jan', 'Feb', 'Mar']
            plt.xlabel('Spring')
        elif season == 'Sum':
            xticks_labels = ['Apr', 'May', 'Jun']
            plt.xlabel('Summer')
        elif season == 'Aut':
            xticks_labels = ['Jul', 'Aug', 'Sept']
            plt.xlabel('Autumn')
        elif season == 'Win':
            xticks_labels = ['Oct', 'Nov', 'Dec']
            plt.xlabel('Winter')
        else:
            assert False, 'season wrong!!!'
        plt.xticks(np.linspace(15*24, len(x)-15*24, len(xticks_labels)),
                   xticks_labels)
        plt.yticks(ynew_ticks)
        if title != None:
            plt.title(title)
        if filepath != None:
            plt.savefig(filepath, format=format)
        plt.show()


if __name__ == '__main__':
    LEN = 24*91
    x = np.arange(0, LEN)
    y = np.random.normal(size=(50, LEN))
    # draw_SLPs(x, y, 'Spr')
    # draw_SLPs(x, y, 'Spr', cluster_center=np.random.rand(LEN))
    draw_SLPs(x, y, cluster_center=np.random.rand(LEN))