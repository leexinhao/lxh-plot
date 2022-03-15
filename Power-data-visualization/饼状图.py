# -*- coding: utf-8 -*-
"""
画饼状图
@author: lxh
"""
import numpy as np
import matplotlib.pyplot as plt


def draw_pie(datas, labels, label_title=None, title=None, filepath=None, formats=('svg')):

    # with plt.style.context('seaborn-paper'):
    plt.rcParams['font.family'] = ['Times New Roman']
    # label_font = {
    #     # 'weight': 'bold',
    #     'size': 18,
    #     'family': 'Times New Roman'
    # }
    fig, ax = plt.subplots(figsize=(7, 4), subplot_kw=dict(aspect="equal"))
    explode = [0.02] * len(labels)
    # maxi = 0
    # for i in range(len(datas)):
    #     if datas[i] > datas[maxi]:
    #         maxi = i
    # explode[maxi] = 0.1
    colors = plt.get_cmap('Set1').colors
    wedges, texts, autotexts = ax.pie(datas, autopct='%1.1f%%',
                                    #   textprops={'color': "w"},
                                      explode=explode,
                                      #   shadow=True,
                                      colors=colors,
                                      startangle=90)

    ax.legend(wedges, labels,
              title=label_title,
            #   loc="lower center",
              loc=1,
              frameon=False,
              ncol=4,
              handletextpad=0.1,
              columnspacing=0.7,
              bbox_to_anchor=(0.6, 0, 0.5, 1),
              prop={'size': 10, 'weight':'bold'})

    plt.setp(autotexts, size=15, weight="bold")

    if title != None:
        ax.set_title(title)

    if filepath != None:
        for format in formats:
            plt.savefig(filepath+'.'+format, format=format, dpi=300)
    plt.show()


if __name__ == '__main__':
    recipe = ["375aMDTP 1",
              "275aMDTP 2",
              "250aMDTP 3",
              "300aMDTP 4"]

    datas = [float(x.split('a')[0]) for x in recipe]
    labels = [x.split('a')[-1] for x in recipe]
    draw_pie(datas, labels, filepath="./dsad.tif",
             formats=('svg', 'png', 'tif'))
