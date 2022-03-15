# -*- coding: utf-8 -*-
"""
画LP曲线图
@author: lxh
"""

import numpy as np
import matplotlib.pyplot as plt


def draw_LPs(x, LPs, LP_type, ymax=None, pure=False, cluster_center=None, lt_title=None,
              title=None, filepath=None, formats=None, color='#C8C8FF', c_color='#8B0000'):
    r'''
    x: 曲线维度，为24,48,96等
    LPs: LP数组或ndarray
    cluster_center: 聚类中心曲线，对于KMeans聚类来说好像就是平均的
    pure: 为False画彩色的
    默认会画一条平均值曲线
    '''
    assert LP_type == 'DLP' or LP_type == 'WLP' or LP_type == 'MLP' or LP_type == 'YLP'
    xlabel_dict = {'DLP': 'Time', 'WLP': 'Day', 'MLP': 'Day', 'YLP': 'Month'}
    LP_width_dict = {'DLP': 0.5, 'WLP': 0.5, 'MLP': 0.5, 'YLP': 0.3}
    C_width_dict = {'DLP': 4, 'WLP': 1.5, 'MLP': 1, 'YLP': 0.4}

    plt.rcParams['font.family'] = ['Times New Roman']
    label_font = {
        # 'weight': 'bold',
        'size': 18,
        'family': 'Times New Roman'
    }
    LPs = np.array(LPs)
    if ymax == None:
        ymax = int(LPs.max()) + 1
    fig = plt.figure(figsize=(8, 6))
    x = np.array(x)
    assert len(x) == LPs.shape[1]

    for LP in LPs:
        if pure:
            plt.plot(x, LP, color=color, linewidth=LP_width_dict[LP_type])
        else:
            plt.plot(x, LP, linewidth=LP_width_dict[LP_type])
    ax = fig.gca()
    if pure:
        if np.any(cluster_center) != None:
            plt.plot(x, cluster_center, color=c_color,
                     linewidth=C_width_dict[LP_type], label='Cluster Center')
        else:
            # 用平均值代替聚类中心
            plt.plot(x, LPs.mean(axis=0), color=c_color,
                     linewidth=C_width_dict[LP_type], label='Cluster Center')

    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    plt.xlim((-1, len(x)))
    plt.ylim((0, ymax))
    plt.xlabel(xlabel_dict[LP_type], fontdict=label_font)
    plt.ylabel('Power consumption (kWh)', fontdict=label_font)
    plt.tick_params(axis='x')
    plt.tick_params(axis='y')
    ynew_ticks = np.linspace(0, ymax, 10)
    plt.yticks(ynew_ticks, fontsize=13)

    if LP_type == 'DLP':
        plt.xticks(np.arange(len(x)/24, len(x) + len(x)/24, len(x)/12),
                ['01:00',  '03:00', '05:00',  '07:00',
                    '09:00', '11:00', '13:00', '15:00',
                    '17:00',  '19:00',  '21:00', '23:00'], fontsize=13)
    elif LP_type == 'WLP':
        xticks_labels = ['Sun', 'Mon', 'Tues',
                         'Wed', 'Thu', 'Fri', 'Sat']
        plt.xticks(np.linspace(12, len(x)-12, len(xticks_labels)),
                xticks_labels, fontsize=13)
    elif LP_type == 'MLP':
        xticks_labels = ['1', '3', '5', '7', '9', '11',
                         '13', '15', '17', '19', '21', '23',
                         '25', '27', '29', '31']
        plt.xticks(np.linspace(0, len(x), len(xticks_labels)),
                xticks_labels, fontsize=13)
    elif LP_type == 'YLP':
        plt.xticks(np.linspace(48, len(x), 12),
        ['Jan',  'Feb', 'Mar',  'Apr',
            'May', 'Jun', 'Jul', 'Aug',
            'Sept',  'Oct',  'Nov', 'Dec'], fontsize=13)   
    
    if title is not None:
        plt.title(title, fontdict=label_font)
    if lt_title is not None:
        plt.text(0.11, 0.93, lt_title, fontdict=dict(fontsize=20,
                                                     color='r', family='DejaVu Sans',
                                                     weight='bold'),
                 ha='center', va='center', transform=ax.transAxes)
    if filepath is not None and formats is not None:
        for format in formats:
            plt.savefig(filepath+'.'+format, format=format)
    plt.show()


if __name__ == '__main__':
    LEN = 24 * 365
    x = np.arange(0, LEN)
    y = np.random.normal(size=(500, LEN)) + 5
    # draw_LPs(x, y, LP_type='DLP', pure=True,
    #          cluster_center=np.random.rand(LEN)+5, title='one color')
    draw_LPs(x, y, LP_type='YLP', pure=True,
             cluster_center=np.random.rand(LEN)+5, title='one color')
    # color_list = [('c', 'r'), ('tan', 'r'), ('lime', 'r'), ('b', 'r'),
    #               ('gold', 'r'), ('limegreen', 'r'), ('darkblue', 'r'), ('yellowgreen', 'r')]
    # for i, colors in enumerate(color_list):
    #     draw_LPs(x, y, pure=True,
    #               color=colors[0], c_color=colors[1], lt_title="DTLP1")
    
