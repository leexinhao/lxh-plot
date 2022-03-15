import numpy as np
import matplotlib.pyplot as plt
'''
需要python3.9版本以上
'''


def draw_center_users_barv(datas, label1='Cluster', label2='Cluster',
                           title=None, filepath=None, formats=None, label_font=None):
    plt.figure(figsize=(8, 6))
    if label_font is None:
        label_font = {
            # 'weight': 'bold',
            'size': 18,
            'family': 'Times New Roman'
        }
    datas = np.array(datas).T  # 这是个蠢操作但是我下面代码懒得改了
    plt.rcParams['font.family'] = ['Times New Roman']
    labels = [label1 + " " + str(i+1) for i in range(len(datas[0]))]

    x = range(len(labels))
    width = 0.5

    # 将bottom_y元素都初始化为0
    bottom_y = np.zeros(len(labels))

    # 按列计算计算每组柱子的总和，为计算百分比做准备
    sums = np.sum(datas, axis=0)
    for i, data in enumerate(datas):
        # 计算每个柱子的高度，即百分比
        y = data / sums
        plt.bar(x, y, width, bottom=bottom_y, label=label2+' '+str(i+1))
        # 计算bottom参数的位置
        bottom_y = y + bottom_y
    if len(datas) > 4:
        plt.legend(ncol=4, bbox_to_anchor=(0.5, 1.16), frameon=False,
                   loc='upper center', prop={'size': 15})
    else:
        plt.legend(ncol=len(datas[0]), bbox_to_anchor=(0.5, 1.12), frameon=False,
                   loc='upper center', prop={'size': 15})
    plt.xticks(x, labels, fontsize=15)
    plt.yticks(fontsize=15)
    plt.ylabel('Proportion', fontsize=15)
    if title is not None:
        plt.title(title, fontdict=label_font)
    if filepath is not None and formats is not None:
        for format in formats:
            plt.savefig(filepath+'.'+format, format=format, dpi=300)
    plt.show()


if __name__ == "__main__":
    # DTLP1 = [20, 34, 30, 35, 27]
    # DTLP2 = [225, 32, 34, 20, 25]
    # DTLP3 = [21, 31, 37, 21, 28]
    # DTLP4 = [26, 31, 35, 27, 21]
    # datas = np.array([DTLP1, DTLP2, DTLP3, DTLP4]).T
    datas = np.array([[116.68932038834951, 284.3009708737864, 0.0048543689320388345, 57.65533980582524, 0.0048543689320388345, 297.4466019417476, 98.37378640776699, 240.14077669902912],
                      [52.566292134831464, 259.54606741573036, 0.0, 5.602247191011236,
                          0.017977528089887642, 306.2584269662921, 367.0494382022472, 103.68988764044944],
                      [94.66666666666667, 263.5353535353535, 36.505050505050505, 124.91919191919192,
                          73.48484848484848, 228.16161616161617, 106.78787878787878, 163.6161616161616],
                      [0.04081632653061224, 512.0408163265306, 0.0, 0.0, 0.0,
                       204.18367346938774, 371.3469387755102, 1.6326530612244898],
                      [91.06122448979592, 320.7142857142857, 4.591836734693878, 196.87755102040816,
                       27.387755102040817, 188.0204081632653, 48.38775510204081, 217.9591836734694],
                      [169.83333333333334, 306.9583333333333, 0.0, 119.58333333333333,
                       0.08333333333333333, 235.54166666666666, 256.25, 6.75],
                      [108.40625, 321.0625, 0.0, 19.34375, 0.0, 291.40625, 349.28125, 3.109375]])
    draw_center_users_barv(datas, label1='DMTP', label2='DLTP')
