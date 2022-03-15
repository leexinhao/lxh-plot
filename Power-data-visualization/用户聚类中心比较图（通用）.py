# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt


def draw_center_users(K_user, K_load, center_users, ymax=None, label1='Cluster', label2='Cluster',
                      title=None, filepath=None, formats=None, label_font=None):
    r'''
    K_user: 用户聚类数K
    K_load: 曲线聚类数K
    center_users: 聚类中心数组
    '''
    if label_font is None:
        label_font = {
            # 'weight': 'bold',
            'size': 18,
            'family': 'Times New Roman'
        }
    assert K_user == len(center_users)
    plt.rcParams['font.family'] = ['Times New Roman']

    if ymax == None:
        ymax = int(center_users.max()) + 1
    plt.figure(figsize=(8, 6))
    center_users = np.array(center_users)
    x = np.arange(1, K_load+1, dtype=np.int)
    assert len(x) == center_users.shape[1]

    for i, user in enumerate(center_users):
        plt.plot(x, user, label=label1+" "+str(i+1),
                 linewidth=2)

    ax = plt.gca()

    plt.legend(loc=1, prop={'size': 15})
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    plt.xlim((0.5, len(x)+0.5))
    plt.ylim((0, ymax))
    # plt.xlabel(xlabel_dict[user_type], fontdict=label_font)
    plt.ylabel('Number of typical load patterns', fontdict=label_font)
    plt.tick_params(axis='x')
    plt.tick_params(axis='y')
    plt.xticks(x,
               [label2+" "+str(i) for i in range(1, K_load+1)], fontsize=15)
    ynew_ticks = np.arange(0, ymax, max(1, ymax//10))
    plt.yticks(ynew_ticks, fontsize=15)

    if title is not None:
        plt.title(title, fontdict=label_font)
    if filepath is not None and formats is not None:
        for format in formats:
            plt.savefig(filepath+'.'+format, format=format)
    plt.show()


if __name__ == '__main__':
    K = 6
    y = np.random.normal(size=(4, K)) * 20

    draw_center_users(4, K, y, label1='MMTP', label2='MLTP')
