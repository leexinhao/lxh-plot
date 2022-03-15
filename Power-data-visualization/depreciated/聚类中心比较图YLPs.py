# -*- coding: utf-8 -*-
"""
画YLP聚类中心比较图
@author: lxh
"""

import pickle
import sys
import os
import numpy as np
import matplotlib.pyplot as plt




def draw_center_YLPs(x, center_YLPs, ymax=None,
              title=None, filepath=None, formats=('svg')):
    r'''
    x: 曲线维度，为24,48,96等
    center_YLPs: 聚类中心数组
    '''
    plt.rcParams['font.family'] = ['Times New Roman']
    label_font = {
        # 'weight': 'bold',
        'size': 18,
        'family': 'Times New Roman'
    }
    # with plt.style.context('science'):
    if ymax == None:
        ymax = int(center_YLPs.max()) + 1
    plt.figure(figsize=(8, 6))
    center_YLPs = np.array(center_YLPs)
    x = np.array(x)
    assert len(x) == center_YLPs.shape[1]

    for i, YLP in enumerate(center_YLPs):
        plt.plot(x, YLP, label='Cluster '+str(i+1), linewidth=0.5)

    ax = plt.gca()

    # ax.spines['right'].set_color('none')
    # ax.spines['top'].set_color('none')

    plt.legend(loc=1, prop={'size': 15})
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    plt.xlim((0, len(x)))
    plt.ylim((0, ymax))
    plt.xlabel('Month', fontdict=label_font)
    plt.ylabel('Power consumption (kWh)', fontdict=label_font)
    plt.tick_params(axis='x')
    plt.tick_params(axis='y')
    ynew_ticks = np.linspace(0, ymax, 10)

    plt.xticks(np.linspace(48, len(x), 12),
            ['Jan',  'Feb', 'Mar',  'Apr',
                'May', 'Jun', 'Jul', 'Aug',
                'Sept',  'Oct',  'Nov', 'Dec'], fontsize=13)
    plt.yticks(ynew_ticks, fontsize=13)
    if title != None:
        plt.title(title, fontdict=label_font)
    if filepath != None:
        for format in formats:
            plt.savefig(filepath+'.'+format, format=format)
    plt.show()


if __name__ == '__main__':
    LEN = 24 * 365
    x = np.arange(0, LEN)
    y = np.random.normal(size=(4, LEN))
    for j in range(0, LEN, 2):
        y[:, j] = y[:, j+1]  # 平滑曲线
    for i in range(4):
        y[i, :] += 2*i+5
    draw_center_YLPs(x, y)
    # draw_center_YLPs(x, y, filepath='./负荷曲线图center_YLPs示例.svg')
