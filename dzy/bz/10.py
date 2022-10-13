import pandas
from pyecharts.charts import Bar
from pyecharts.charts import EffectScatter
from pyecharts.charts import Line

if __name__ == '__main__':
    data = pandas.read_excel('C:/Users/93601/Code/python/dzy/bz/全国总人口10年数据.xls').iloc[1:6, :].reset_index(
        drop=True)
    # 提取有用部份的数据，并标准化索引
    data = data.set_axis(data.iloc[0], axis=1, inplace=False).drop(index=0).reset_index(drop=True).set_index('指标',
                                                                                                             drop=True)
    # 柱状图
    bar = Bar()
    bar.add_xaxis(data.columns.tolist()[::-1])
    for i in data.index:
        bar.add_yaxis(i, data.loc[i].tolist()[::-1])
    bar.render('C:/Users/93601/Code/python/dzy/bz/10_bar.html')

    # 折线图
    line = Line()
    line.add_xaxis(data.columns.tolist()[::-1])
    for i in data.index:
        line.add_yaxis(i, data.loc[i].tolist()[::-1])
    line.render('C:/Users/93601/Code/python/dzy/bz/10_line.html')

    # 类散点图
    effect = EffectScatter()
    effect.add_xaxis(data.columns.tolist()[::-1])
    for i in data.index:
        effect.add_yaxis(i, data.loc[i].tolist()[::-1])
    effect.render('C:/Users/93601/Code/python/dzy/bz/10_effect.html')
