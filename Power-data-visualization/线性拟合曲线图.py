# -*- coding: utf-8 -*-
"""
线性拟合加误差填充加散点
画图前记得x单调排序，因为有plot，参考代码如下
x: list y: list
newlist = zip(x, y)
newlist = sorted(newlist, key=lambda k: [k[0], k[1]])
x = []
y = []
for list in newlist:
    x.append(list[0])
    y.append(list[1])
@author: lxh
"""
import numpy as np
import matplotlib.pyplot as plt


def draw_linear_fit(x, y, a=None, b=None, xlabel=None, ylabel=None, title=None, filepath=None):
    with plt.style.context('science'):
        plt.figure(figsize=(6, 5))
        x = np.array(x).reshape(-1)
        y = np.array(y).reshape(-1)
        if a == None or b == None:
            # fit a linear curve an estimate its y-values and their error.
            a, b = np.polyfit(x, y, deg=1)
        y_est = a * x + b
        y_err = x.std() * np.sqrt(1/len(x) +
                                  (x - x.mean())**2 / np.sum((x - x.mean())**2))
        plt.plot(x, y_est, '-')
        plt.fill_between(x, y_est - y_err, y_est + y_err, alpha=0.2)
        plt.plot(x, y, 'o', color='tab:brown')

        if xlabel != None:
            plt.xlabel(xlabel)
        if ylabel != None:
            plt.ylabel(ylabel)
        if title != None:
            plt.title(title)

        if filepath != None:
            plt.savefig(filepath, format=format)

        plt.show()

if __name__ == '__main__':
    x = np.linspace(0, 10, 11)
    y = [3.9, 4.4, 10.8, 10.3, 11.2, 13.1, 14.1, 9.9, 13.9, 15.1, 12.5]
    draw_linear_fit(x, y, xlabel='x', ylabel='y', title='linear fit')
