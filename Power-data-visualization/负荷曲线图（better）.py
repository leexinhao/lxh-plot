# -*- coding: utf-8 -*-
"""
画LP曲线图
@author: lxh
"""

import numpy as np
import matplotlib.pyplot as plt


def draw_LPs_new(x, LPs, LP_type, ymax=None, pure=False, cluster_center=None, lt_title=None,
                 title=None, filepath=None, formats=None, color='#C8C8FF', c_color='#8B0000', dpi=300, fontsize=25):
    r'''
    x: 曲线维度，为24,48,96等
    LPs: LP数组或ndarray
    cluster_center: 聚类中心曲线，对于KMeans聚类来说好像就是平均的
    pure: 为False画彩色的
    默认会画一条平均值曲线
    '''
    assert LP_type == 'DLP' or LP_type == 'WLP' or LP_type == 'MLP' or LP_type == 'YLP'
    xlabel_dict = {'DLP': 'Hour of the day', 'WLP': 'Day of the week',
                   'MLP': 'Day of the month', 'YLP': 'Month of the year'}
    LP_width_dict = {'DLP': 0.5, 'WLP': 0.5, 'MLP': 0.5, 'YLP': 0.3}
    C_width_dict = {'DLP': 8, 'WLP': 3, 'MLP': 2, 'YLP': 0.4}

    fig = plt.figure(figsize=(8, 7), dpi=dpi)

    plt.rcParams['font.family'] = ['Times New Roman']
    label_font = {
        # 'weight': 'bold',
        'size': fontsize,
        'family': 'Times New Roman'
    }

    LPs = np.array(LPs)
    if ymax == None:
        ymax = int(LPs.max()) + 1

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
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['left'].set_linewidth(2)
    ax.spines['right'].set_linewidth(2)
    ax.spines['top'].set_linewidth(2)

    # plt.minorticks_on()
    plt.xlabel(xlabel_dict[LP_type], fontdict=label_font)
    plt.ylabel('Power consumption (kWh)', fontdict=label_font)
    if LP_type == 'WLP':
        plt.tick_params(which='major', axis='x', width=1,
                        length=5, direction='in', color='#C0C0C0')
        plt.tick_params(which='minor', axis='x', width=1,
                        length=5, direction='in', color='#C0C0C0')
    else:
        plt.tick_params(which='major', axis='x', width=1,
                        length=8, direction='out')
        plt.tick_params(which='minor', axis='x', width=1,
                        length=5, direction='out')

    plt.tick_params(which='major', axis='y', width=1, length=8)
    plt.tick_params(which='minor', axis='y', width=1, length=0)

    def get_step(n):
        if n > 10:
            return (n+5) // 10
        elif n > 5:
            return 1
        else:
            return 0.5

    ymax = int(ymax)
    if ymax % 2 == 0:
        ymax += 2
    else:
        ymax += 1
    yticks_labels = [str(i) for i in np.arange(
        0, ymax+1, get_step(ymax))] 
    plt.yticks(np.arange(0, ymax+1, get_step(ymax)),
               yticks_labels, fontsize=fontsize)
    plt.xlim((0, len(x)-1))
    plt.ylim((-ymax/60, ymax))

    if LP_type == 'DLP':
        plt.xticks(np.arange(0, len(x), len(x)/6),
                   ['0', '4', '8', '12', '16', '20'], fontsize=fontsize)
    elif LP_type == 'WLP':
        xticks_labels = ['Sun', 'Mon', 'Tues',
                         'Wed', 'Thu', 'Fri', 'Sat']
        fg = np.linspace(0, len(x), len(xticks_labels)+1)
        for vx in fg[1:-1]:
            plt.vlines(vx, -ymax/60, ymax, linestyle='dashed', color='#C0C0C0')
        # plt.grid(True, linestyle='dashed', axis='x', color='#C0C0C0')
        plt.minorticks_on()
        delta = (fg[1] - fg[0]) / 2
        plt.xticks(fg[0:-1]+delta, xticks_labels, fontsize=fontsize)
        # plt.xticks(np.linspace(len(x)/(7*2), len(x)-len(x)/(7*2), len(xticks_labels)),
        #            xticks_labels, fontsize=fontsize)
        # xticks_labels = ['Sun', 'Tues', 'Thu', 'Sat']
        # plt.xticks(np.arange(0, len(x), len(x)*2/7),
        #            xticks_labels, fontsize=fontsize)
    elif LP_type == 'MLP':
        xticks_labels = ['1', '5', '9', '13', '17',
                         '21', '25', '29']
        plt.xticks(np.linspace(len(x)/(31*2), len(x)-len(x)/(31*2), len(xticks_labels)),
                   xticks_labels, fontsize=fontsize)
    elif LP_type == 'YLP':
        plt.xticks(np.linspace(len(x)/(12*2), len(x)-len(x)/(12*2), 12),
                   ['Jan',  'Feb', 'Mar',  'Apr',
                    'May', 'Jun', 'Jul', 'Aug',
                    'Sept',  'Oct',  'Nov', 'Dec'], fontsize=fontsize-6)

        # plt.xticks(np.arange(0, len(x), len(x)*2/12),
        #            ['Jan',  'Mar', 'May',  'Jul', 'Sept',  'Nov', ], fontsize=fontsize)

    if title is not None:
        plt.title(title, fontdict=label_font)
    if lt_title is not None:
        plt.text(0.11, 0.93, lt_title, fontdict=dict(fontsize=fontsize,
                                                     color='r', family='DejaVu Sans',
                                                     weight='bold'),
                 ha='center', va='center', transform=ax.transAxes)
    if filepath is not None and formats is not None:
        for format in formats:
            plt.savefig(filepath+'.'+format, format=format, dpi=dpi)
    # plt.show()


if __name__ == '__main__':
    LEN = 24*7
    x = np.arange(0, LEN)
    y = np.random.normal(size=(5, LEN)) + 40  
    # draw_LPs(x, y, LP_type='DLP', pure=True,
    #          cluster_center=np.random.rand(LEN)+5, title='one color')
    # draw_LPs_new(x, y, LP_type='WLP', pure=True,
    #              cluster_center=np.random.rand(LEN)+5, title='one color')
    draw_LPs_new(x, y, LP_type='WLP', pure=True, ymax=45,
                  title='one color', filepath="./aa", formats=('svg', 'png', 'tif'))
    # color_list = [('c', 'r'), ('tan', 'r'), ('lime', 'r'), ('b', 'r'),
    #               ('gold', 'r'), ('limegreen', 'r'), ('darkblue', 'r'), ('yellowgreen', 'r')]
    # for i, colors in enumerate(color_list):
    #     draw_LPs(x, y, pure=True,
    #               color=colors[0], c_color=colors[1], lt_title="DTLP1")
