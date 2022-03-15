# 导入用到的包
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl

file = r'/Users/caizhiming/Downloads/fz2019.xlsx'
df = pd.read_excel(file, sheet_name='Sheet1', index_col='月份')
df.head(10)

# mpl.rcParams['font.sans-serif'] = ['SimHei']   #设置简黑字体
mpl.rcParams['font.sans-serif'] = ['Songti SC']
mpl.rcParams['axes.unicode_minus'] = False


# 自定义黄色颜色
y = np.array([255, 255, 0])/255
colors = ['tab:green', y, 'orange', 'red']
# 自由设定颜色区间
bounds = [0, 60, 100, 180, 300]
# bounds = [0, 75, 150, 225, 300] # 也可以均匀划分
cm_light = mpl.colors.ListedColormap(colors)
norm = mpl.colors.BoundaryNorm(bounds, cm_light.N)

plt.figure(figsize=(22, 6))
# cbar_kws设定颜色标尺的ticks线性分布, mask标记过滤值
ax = sns.heatmap(df, square=True, annot=True, vmin=0, vmax=200, fmt='.0f', linewidths=.05,
                 linecolor='gray', mask=df < 30, cmap=cm_light, norm=norm,
                 cbar_kws={'ticks': bounds, 'spacing': 'proportional'})


# 防止显示不全（有的版本及操作系统会遇到这个问题）
plt.ylim(0, len(df)+.5)
plt.xlim(0, len(df.columns)+0.5)
plt.show()
