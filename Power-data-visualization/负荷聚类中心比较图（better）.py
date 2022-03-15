# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


def draw_center_LPs_new(x, center_LPs, LP_type, ymax=None, label='Cluster',
                        title=None, filepath=None, formats=None, dpi=300, fontsize=25):
    r'''
    x: 曲线维度，为24,48,96等
    center_LPs: 聚类中心数组
    '''
    assert LP_type == 'DLP' or LP_type == 'WLP' or LP_type == 'MLP' or LP_type == 'YLP'
    xlabel_dict = {'DLP': 'Time', 'WLP': 'Day', 'MLP': 'Day', 'YLP': 'Month'}
    LP_width_dict = {'DLP': 3, 'WLP': 2.5, 'MLP': 2, 'YLP': 1.5}

    plt.rcParams['font.family'] = ['Times New Roman']
    label_font = {
        # 'weight': 'bold',
        'size': fontsize,
        'family': 'Times New Roman'
    }
    center_LPs = np.array(center_LPs)
    x = np.array(x)
    if ymax == None:
        ymax = int(center_LPs.max()) + 1

    fig = plt.figure(figsize=(8, 7), dpi=dpi)

    plt.rcParams['font.family'] = ['Times New Roman']
    label_font = {
        # 'weight': 'bold',
        'size': fontsize,
        'family': 'Times New Roman'
    }


    assert len(x) == center_LPs.shape[1]

    for i, LP in enumerate(center_LPs):
        plt.plot(x, LP, label=label+" "+str(i+1),
                 linewidth=LP_width_dict[LP_type])

    ax = plt.gca()

    plt.legend(prop={'size': fontsize-5},  bbox_to_anchor=(0.5, 1.2), frameon=False,
               loc='upper center', ncol=3, labelspacing=0.4, columnspacing=0.4)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

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

    ymax = int(ymax)
    if ymax % 2 == 0:
        ymax += 2
    else:
        ymax += 1
    yticks_labels = [str(i) for i in range(0, ymax+1, 2)]
    plt.yticks(np.arange(0, ymax+1, 2),
               yticks_labels, fontsize=fontsize)
    plt.xlim((0, len(x)-1))
    plt.ylim((-0.5, ymax))
    

    if LP_type == 'DLP':
        plt.xticks(np.arange(0, len(x), len(x)/6),
                   ['0', '4', '8', '12', '16', '20'], fontsize=fontsize)
    elif LP_type == 'WLP':
        xticks_labels = ['Sun', 'Mon', 'Tues',
                         'Wed', 'Thu', 'Fri', 'Sat']
        fg = np.linspace(0, len(x), len(xticks_labels)+1)
        for vx in fg[1:-1]:
            plt.vlines(vx ,-0.5, ymax, linestyle='dashed',color='#C0C0C0')
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

    if title is not None:
        plt.title(title, fontdict=label_font)
    if filepath is not None and formats is not None:
        for format in formats:
            plt.savefig(filepath+'.'+format, format=format, dpi=dpi)
    plt.show()


if __name__ == '__main__':
    LEN = 24 * 31
    x = np.arange(0, LEN)
    y = np.random.normal(size=(4, LEN))
    for j in range(0, LEN, 2):
        y[:, j] = y[:, j+1]  # 平滑曲线
    for i in range(4):
        y[i, :] += 2*i+5
    draw_center_LPs_new(x, y, LP_type='MLP', label='MLTP')
    # draw_center_LPs(x, y, filepath='./负荷曲线图center_LPs示例.svg')
