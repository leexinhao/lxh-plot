import numpy as np
import matplotlib.pyplot as plt

def draw_line(x, y, ymax=None, xlabel=None, ylabel=None,
                     title=None, filepath=None, format='svg'):
    with plt.style.context('science'):
        if ymax == None:
            ymax = int(y.max()) + 1
        plt.figure(figsize=(8, 4))
        
        x = np.array(x)
        y = np.array(y)
 
        plt.plot(x, y, linewidth=0.4)

        ax = plt.gca()

        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')

        # plt.legend(loc=1)
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')

        plt.xlim((0, len(x)))
        plt.ylim((0, ymax))
        if xlabel != None:
            plt.xlabel(xlabel)
        plt.ylabel('Power consumption (kWh)')
        plt.tick_params(axis='x')
        plt.tick_params(axis='y')
        ynew_ticks = np.linspace(0, ymax, 10)

        # plt.xticks(x,
        #            [str(xx) for xx in x])
        # plt.yticks(ynew_ticks)
        # plt.setp(ax.get_xticklabels(), rotation=30, ha="right")
        if title != None:
            plt.title(title)
        if filepath != None:
            plt.savefig(filepath, format=format)
        plt.show()


if __name__ == '__main__':

    x = np.arange(1920, 2021)
    y = np.linspace(0, 1, len(x))
    draw_line(x, y)

