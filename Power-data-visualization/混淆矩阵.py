import seaborn as sns
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt


def draw_confusion_matrix(y_true, y_pred, xlabel=None, ylabel=None,
                             title=None, filepath=None, format='svg'):
    with plt.style.context('science'):
        sns.set()
        f, ax = plt.subplots()
        C2 = confusion_matrix(y_true, y_pred, labels=[0, 1, 2])
        sns.heatmap(C2, annot=True, ax=ax)  # 画热力图

        if title != None:
            ax.set_title(title)  # 标题
        if xlabel != None:
            ax.set_xlabel(xlabel)  # x轴
        if ylabel != None:
            ax.set_ylabel(ylabel)  # y轴
        if title != None:
            plt.title(title)
        if filepath != None:
            plt.savefig(filepath, format=format)
        plt.show()

if __name__ == '__main__':
    y_true = [0, 0, 1, 2, 1, 2, 0, 2, 2, 0, 1, 1]
    y_pred = [1, 0, 1, 2, 1, 0, 0, 2, 2, 0, 1, 1]
    xlabel = 'predict'
    ylabel = 'true'
    title = 'confusion matrix'
    draw_confusion_matrix(y_true, y_pred, xlabel, ylabel, title)
