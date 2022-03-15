# -*- coding: utf-8 -*-
"""
雷达图
@author: lxh
"""
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import copy

def draw_radar(data, data_labels, radar_labels, title=None, filepath=None, format='svg'):
    with plt.style.context('ggplot'):
        data = np.array(data)
        assert data.shape[0] == len(
            data_labels) and data.shape[1] == len(radar_labels)
        # for i in range(data.shape[1]):
        #     tmp = data[:, i].min()
        #     data[:, i] -= tmp
        #     data[:, i] += np.abs(tmp)  # 防止有负值出现
        from sklearn.preprocessing import MinMaxScaler
        # print(data)
        mm = MinMaxScaler()
        # data = normalize(data, norm='l2')
        data = mm.fit_transform(data)
        # print(data)
        data = data.T
        # 分割圆周长，使其闭合
        angles = np.linspace(0, 2 * np.pi, len(radar_labels), endpoint=False)
        data = np.concatenate((data, [data[0]]))
        angles = np.concatenate((angles, [angles[0]]))
        fig = plt.figure(facecolor="white")
        plt.subplot(111, polar=True)
        plt.plot(angles, data, 'o-', linewidth=1)
        plt.fill(angles, data, alpha=0.25)
        radar_labels.append(radar_labels[0])  # 要保证数据闭合
        plt.thetagrids(angles * 180 / np.pi, radar_labels)
        if title != None:
            plt.figtext(0.52, 0.95, title, ha='center', size=20)
        legend = plt.legend(data_labels, loc=(0.94, 0.80), labelspacing=0.1)
        plt.setp(legend.get_texts(), fontsize='large')
        plt.grid(True)
        plt.show()
        if filepath != None:
            plt.savefig(filepath, format=format)

if __name__ == '__main__':
    # 测试draw_radar
    matplotlib.rcParams['font.family'] = 'SimHei'
    radar_labels = ['研究型(I)', '艺术型(A)', '社会型(S)',
                    '企业型(E)', '常规型(C)', '现实型(R)']  # 雷达标签
    data = np.array([[0.40, 0.32, 0.35, 0.30, 0.30, 0.88],
                     [0.85, 0.35, 0.30, 0.40, 0.40, 0.30],
                     [0.43, 0.89, 0.30, 0.28, 0.22, 0.30],
                     [0.30, 0.25, 0.48, 0.85, 0.45, 0.40]])
    #  [0.20, 0.38, 0.87, 0.45, 0.32, 0.28],
    #  [0.34, 0.31, 0.38, 0.40, 0.92, 0.28]])  # 数据值
    data_labels = ('艺术家', '实验员', '工程师', '推销员')  # , '社会工作者', '记事员')
    draw_radar(data=data, data_labels=data_labels,
               radar_labels=radar_labels)
