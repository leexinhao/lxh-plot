# -*- coding: utf-8 -*-
"""
画MLP聚类中心比较图
@author: lxh
"""

from matplotlib.legend import Legend
import numpy as np
import matplotlib.pyplot as plt


def draw_center_MLPs(x, center_MLPs, ymax=None,
                      title=None, filepath=None, formats=('svg')):
    r'''
    x: 曲线维度，为24x31,48x31,96x31等
    center_MLPs: 聚类中心数组
    '''
    # with plt.style.context('science'):
    plt.rcParams['font.family'] = ['Times New Roman']
    label_font = {
        # 'weight': 'bold',
        'size': 18,
        'family': 'Times New Roman'
    }
    if ymax == None:
        ymax = int(center_MLPs.max()) + 1
    plt.figure(figsize=(8, 6))
    center_MLPs = np.array(center_MLPs)
    x = np.array(x)
    assert len(x) == center_MLPs.shape[1]

    for i, MLP in enumerate(center_MLPs):
        plt.plot(x, MLP, label='Cluster '+str(i+1), linewidth=1)

    ax = plt.gca()
    plt.legend(loc=1, prop={'size': 15})
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    
    plt.xlim((0, len(x)))
    plt.ylim((0, ymax))
    plt.xlabel('Day', fontdict=label_font)
    plt.ylabel('Power consumption (kWh)', fontdict=label_font)
    plt.tick_params(axis='x')
    plt.tick_params(axis='y')
    xticks_labels = ['1', '3', '5', '7', '9', '11',
                    '13', '15', '17', '19', '21', '23',
                    '25', '27', '29', '31']
    plt.xticks(np.linspace(0, len(x), len(xticks_labels)),
            xticks_labels, fontsize=13)
    ynew_ticks = np.linspace(0, ymax, 10)
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
    y = np.random.normal(size=(4, LEN))
    for j in range(0, LEN, 2):
        y[:, j] = y[:, j+1] # 平滑曲线
    for i in range(4):
        y[i, :] += 2*i+5
    draw_center_MLPs(x, y)
    # draw_center_MLPs(x, y, filepath='./负荷曲线图center_MLPs示例.svg')
