# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


def draw_center_LPs(x, center_LPs, LP_type, ymax=None, label='Cluster',
                     title=None, filepath=None, formats=None):
    r'''
    x: 曲线维度，为24,48,96等
    center_LPs: 聚类中心数组
    '''
    assert LP_type == 'DLP' or LP_type == 'WLP' or LP_type == 'MLP' or LP_type == 'YLP'
    xlabel_dict = {'DLP': 'Time', 'WLP': 'Day', 'MLP': 'Day', 'YLP': 'Month'}
    LP_width_dict = {'DLP': 2, 'WLP': 1.5, 'MLP': 1, 'YLP': 0.5}

    plt.rcParams['font.family'] = ['Times New Roman']
    label_font = {
        # 'weight': 'bold',
        'size': 18,
        'family': 'Times New Roman'
    }
    center_LPs = np.array(center_LPs)
    x = np.array(x)
    if ymax == None:
        ymax = int(center_LPs.max()) + 1
    plt.figure(figsize=(8, 6))

    assert len(x) == center_LPs.shape[1]

    for i, LP in enumerate(center_LPs):
        plt.plot(x, LP, label=label+" "+str(i+1), linewidth=LP_width_dict[LP_type])

    ax = plt.gca()

    plt.legend(loc=1, prop={'size': 15})
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
    if filepath is not None and formats is not None:
        for format in formats:
            plt.savefig(filepath+'.'+format, format=format)
    plt.show()


if __name__ == '__main__':
    LEN = 24 * 31
    x = np.arange(0, LEN)
    y = np.random.normal(size=(4, LEN))
    for j in range(0, LEN, 2):
        y[:, j] = y[:, j+1]  # 平滑曲线
    for i in range(4):
        y[i, :] += 2*i+5
    draw_center_LPs(x, y, LP_type='MLP', label='MLTP')
    # draw_center_LPs(x, y, filepath='./负荷曲线图center_LPs示例.svg')
