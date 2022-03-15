# -*- coding: utf-8 -*-
"""
画WLP聚类中心比较图
@author: lxh
"""

import pickle
import sys
import os
import numpy as np
import matplotlib.pyplot as plt




def draw_center_WLPs(x, center_WLPs, ymax=None,
                     title=None, filepath=None, formats=('svg')):
    r'''
    x: 曲线维度，为24x7,48x7,96x7等
    center_WLPs:  聚类中心数组
    '''
    # with plt.style.context('science'):
    plt.rcParams['font.family'] = ['Times New Roman']
    label_font = {
        # 'weight': 'bold',
        'size': 18,
        'family': 'Times New Roman'
    }
    if ymax == None:
        ymax = int(center_WLPs.max()) + 1
    plt.figure(figsize=(8, 6))
    center_WLPs = np.array(center_WLPs)
    x = np.array(x)
    assert len(x) == center_WLPs.shape[1]

    for i, center_WLP in enumerate(center_WLPs):
        plt.plot(x, center_WLP, label='Cluster '+str(i+1), linewidth=1.5)

    ax = plt.gca()

    # ax.spines['right'].set_color('none')
    # ax.spines['top'].set_color('none')

    plt.legend(loc=1, prop={'size': 15})
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    plt.xlim((0, len(x)))
    plt.ylim((0, ymax))
    plt.xlabel('Day', fontdict=label_font)
    plt.ylabel('Power consumption (kWh)', fontdict=label_font)
    plt.tick_params(axis='x')
    plt.tick_params(axis='y')
    ynew_ticks = np.linspace(0, ymax, 10)
    plt.yticks(ynew_ticks, fontsize=13)
    xticks_labels = ['Sun', 'Mon', 'Tues',
                     'Wed', 'Thu', 'Fri', 'Sat']
    plt.xticks(np.linspace(12, len(x)-12, len(xticks_labels)),
               xticks_labels, fontsize=13)
    if title != None:
        plt.title(title, fontdict=label_font)
    if filepath != None:
        for format in formats:
            plt.savefig(filepath+'.'+format, format=format)
    plt.show()


if __name__ == '__main__':
    LEN = 24*7
    x = np.arange(0, LEN)
    y = np.random.normal(size=(5, LEN))
    for i in range(5):
        y[i, :] += 2*i+5

    draw_center_WLPs(x, y)


