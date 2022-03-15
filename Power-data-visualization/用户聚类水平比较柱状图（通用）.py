import numpy as np
import matplotlib.pyplot as plt


def draw_center_users_barh(datas, label1='Cluster', label2='Cluster',
                           title=None, filepath=None, formats=None, label_font=None):
    '''
    需要python3.9版本以上
    '''
    datas = np.array(datas)
    if label_font is None:
        label_font = {
            # 'weight': 'bold',
            'size': 18,
            'family': 'Times New Roman'
        }
    assert len(datas) > 0
    plt.rcParams['font.family'] = ['Times New Roman']
    labels = [label1+' '+str(i+1) for i in range(len(datas))]
    category_names = [label2 + ' '+str(i+1) for i in range(len(datas[0]))]
    datas = datas / datas.mean(axis=1, keepdims=True)
    datas_cum = datas.cumsum(axis=1)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.invert_yaxis()  # 好像是从下往上画的
    # ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(datas, axis=1).max())

    for i, colname in enumerate(category_names):
        widths = datas[:, i]
        starts = datas_cum[:, i] - widths
        rects = ax.barh(labels, widths, left=starts, height=0.5,
                        label=colname)  # , color=color

    if len(datas[0]) > 4:
        plt.legend(ncol=4, bbox_to_anchor=(0.5, 1.16), frameon=False,
                   loc='upper center', prop={'size': 15})
    else:
        plt.legend(ncol=len(datas[0]), bbox_to_anchor=(0.5, 1.1), frameon=False,
                   loc='upper center', prop={'size': 15})

    plt.xticks(np.linspace(0, datas.sum(axis=1).min(), 6),
               ['0', '0.2', '0.4', '0.6', '0.8', '1.0'], fontsize=15)
    plt.yticks(fontsize=15)
    ax.set_xlabel('Proportion', fontsize=15)
    if title is not None:
        plt.title(title, fontdict=label_font)
    if filepath is not None and formats is not None:
        for format in formats:
            plt.savefig(filepath+'.'+format, format=format)
    plt.show()


if __name__ == '__main__':

    # datas = np.array([[10, 15, 17, 32, 20, 6],
    #                   [26, 22, 29, 10, 10, 3],
    #                   [35, 37, 7, 2, 10, 9],
    #                   [32, 11, 9, 15, 30, 3],
    #                   [21, 29, 5, 5, 20, 20],
    #                   [8, 19, 5, 30, 30, 8]]) * 10
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
    # draw_center_users_barh(datas, label1='DMTP', label2='DLTP')
    draw_center_users_barh(datas, label1='DMTP', label2='DLTP',
                           filepath=r'C:\Users\dell\Desktop\test5_3_4_user_水平', formats=('svg', 'png', 'tif'))
