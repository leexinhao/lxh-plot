# -*- coding: utf-8 -*-
"""
画DLP曲线图
@author: lxh
"""

import pickle
import sys
import os
import numpy as np
import matplotlib.pyplot as plt

'''
x: 曲线维度，为24,48,96等
center_DLPs: 聚类中心数组
'''


def draw_center_DLPs(x, center_DLPs, ymax=None, label='Cluster',
                     title=None, filepath=None, formats=None):
    # with plt.style.context('science'):
    plt.rcParams['font.family'] = ['Times New Roman']
    label_font = {
        # 'weight': 'bold',
        'size': 18,
        'family': 'Times New Roman'
    }
    if ymax == None:
        ymax = int(center_DLPs.max()) + 1
    plt.figure(figsize=(8, 6))
    center_DLPs = np.array(center_DLPs)
    x = np.array(x)
    assert len(x) == center_DLPs.shape[1]

    for i, DLP in enumerate(center_DLPs):
        plt.plot(x, DLP, label=label+" "+str(i+1), linewidth=2)

    ax = plt.gca()

    # ax.spines['right'].set_color('none')
    # ax.spines['top'].set_color('none')

    plt.legend(loc=1, prop={'size': 15})
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    plt.xlim((-1, len(x)))
    plt.ylim((0, ymax))
    plt.xlabel('Time', fontdict=label_font)
    plt.ylabel('Power consumption (kWh)', fontdict=label_font)
    plt.tick_params(axis='x')
    plt.tick_params(axis='y')
    ynew_ticks = np.linspace(0, ymax, 10)
    # plt.xticks(np.arange(0, len(x), len(x)/12),
    #            ['00:00',  '02:00', '04:00',  '06:00',
    #             '08:00', '10:00', '12:00', '14:00',
    #             '16:00',  '18:00',  '20:00', '22:00'])
    plt.xticks(np.arange(len(x)/24, len(x) + len(x)/24, len(x)/12),
               ['01:00',  '03:00', '05:00',  '07:00',
                '09:00', '11:00', '13:00', '15:00',
                '17:00',  '19:00',  '21:00', '23:00'], fontsize=13)
    plt.yticks(ynew_ticks, fontsize=13)
    if title is not None:
        plt.title(title, fontdict=label_font)
    if filepath is not None and formats is not None:
        for format in formats:
            plt.savefig(filepath+'.'+format, format=format)
    plt.show()


if __name__ == '__main__':
    LEN = 24
    x = np.arange(0, LEN)
    y = np.random.normal(size=(4, LEN))
    for i in range(4):
        y[i, :] += 2*i+5
    draw_center_DLPs(x, y)
    draw_center_DLPs(x, y, label='DLTP')
    # draw_center_DLPs(x, y, filepath='./负荷曲线图center_DLPs示例.svg')
