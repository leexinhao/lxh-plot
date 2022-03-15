# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from pylab import *

# def autolabel(rects):
#     给柱子上面标值，一般用不上
#     for rect in rects:
#         height = rect.get_height()
#         ax.annotate('{}'.format(height),
#                     xy=(rect.get_x() + rect.get_width() / 2, height),
#                     xytext=(0, 3),  # 3 points vertical offset
#                     textcoords="offset points",
#                     ha='center', va='bottom')
# autolabel(rects1)
# autolabel(rects2)


def draw_loss_bar(loss_values, labels, ymax1=None, ymax2=None, title=None, filepath=None, formats=None):
    '''
    左边RMSE，MAE，右边MAPPE
    '''
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.rcParams['font.family'] = ['Times New Roman']
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))  # dpi=200

    x = np.arange(len(labels))  # the label locations
    width = 0.22  # the width of the bars

    label_font = {
        # 'weight': 'bold',
        'size': 15,
        'family': 'Times New Roman'
    }
    loss_values = np.array(loss_values)
    RMSE = loss_values[0, :]
    MAE = loss_values[1, :]
    MAPPE = loss_values[2, :]
    rects1 = ax.bar(x - width, RMSE, width, label='RMSE', ec='k', color='#E6E7E7', lw=.8
                    )
    rects2 = ax.bar(x, MAE, width, label='MAE', ec='k', color='#6C6E71',
                    lw=.8)

    ax.tick_params(which='major', direction='in', length=5,
                   width=1.5, labelsize=11, bottom=False)
    ax.tick_params(axis='x', labelsize=11, bottom=False)
    ax.set_xticks(x)
    if ymax1 is not None:
        ax.set_ylim(ymin=0, ymax=ymax1)

    ax.set_ylabel('RMSE/MAE (kW)', fontdict=label_font)
    ax.set_xticklabels(labels, fontdict=label_font)
    plt.yticks(fontproperties='Times New Roman', size=14)
    ax.legend(markerscale=15, fontsize=15, frameon=False, loc=2)
    ax.set_xlabel('Dimensionality reduction methods', fontdict=label_font)
    ax2 = ax.twinx()
    plt.yticks(fontproperties='Times New Roman', size=15)
    rects3 = ax2.bar(x + width, MAPPE, width, label='MAPPE', ec='k', color='#a7a9ac', hatch='//',
                     lw=.8)
    ax2.legend(markerscale=15, fontsize=15, frameon=False, loc=1)
    ax2.set_ylabel('MAPPE (%)', fontdict=label_font)
    if ymax2 is not None:
        ax2.set_ylim(ymin=0, ymax=ymax2)

    fig.tight_layout()
    if title is not None:
        plt.title(title, fontdict=label_font)

    if filepath is not None and formats is not None:
        for format in formats:
            plt.savefig(filepath+'.'+format, format=format)
    plt.show()


if __name__ == '__main__':
    # labels = ['PCA', 'AE', 'DAE', 'CNN AE', 'Simple RNN AE', 'GRU AE', 'LSTM AE']
    labels = ['PCA', 'AE', 'DAE', 'CAE', 'LSTM-AE']
    # RMSE = [0.012236991959666823,
    #         0.01565771248346331,
    #         0.010659292061970993,
    #         0.0094828058806568,
    #         0.01576499616333155,
    #         0.00939129985536359,
    #         0.008542491367475256]
    # MAE = [0.009194929677718908,
    #        0.011689612888570441,
    #        0.008054682961523335,
    #        0.00711667491749738,
    #        0.011512766705321142,
    #        0.006657589051874549,
    #        0.0058525305101819435]

    RMSE = [0.012236991959666823,
            0.01565771248346331,
            0.010659292061970993,
            0.00939129985536359,
            0.008542491367475256]
    MAE = [0.009194929677718908,
           0.011689612888570441,
           0.008054682961523335,
           0.00711667491749738,
           0.0058525305101819435]
    MAPPE = [0.009194929677718908,
             0.011689612888570441,
             0.008054682961523335,
             0.00711667491749738,
             0.0058525305101819435]
    draw_loss_bar([RMSE, MAE, MAPPE], labels, ymax1 = 0.02)
