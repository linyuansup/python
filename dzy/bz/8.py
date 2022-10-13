import matplotlib
import requests
import re
import matplotlib.pyplot as plt

if __name__ == '__main__':
    url = 'https://tenapi.cn/resou/'
    # 发送请求
    response = requests.get(url=url)
    # 去除最外层的嵌套
    data = response.json()["list"][:]
    name = []
    num = []
    black = []
    # 标记部分没有热度数值的数据
    for i in range(len(data)):
        if data[i]['hot'] == '':
            black.append(i)
    for i in range(len(data)):
        if i not in black:
            # 如果有热度数，就加入图标
            name.append(data[i]['name'])
            # 有的热度数有分区，去分区信息
            num.append(int((re.sub('[\u4e00-\u9fa5]', '', str(data[i]['hot']))).replace(' ', '')))
    # 设置字体
    font = {'family': 'Microsoft Yahei'}
    matplotlib.rc("font", **font)
    plt.figure(figsize=(20, 40), dpi=160)
    plt.barh(range(len(name)), num, tick_label=name)
    # 设置数据显示
    plt.bar_label(plt.gca().containers[0])
    plt.show()
