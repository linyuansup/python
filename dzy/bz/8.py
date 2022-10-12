import matplotlib
import requests
import re
import matplotlib.pyplot as plt

if __name__ == '__main__':
    url = 'https://tenapi.cn/resou/'
    response = requests.get(url=url)
    data = response.json()["list"][:]
    name = []
    num = []
    black = []
    for i in range(len(data)):
        if data[i]['hot'] == '':
            black.append(i)
    for i in range(len(data)):
        if i not in black:
            name.append(data[i]['name'])
            num.append(int((re.sub('[\u4e00-\u9fa5]', '', str(data[i]['hot']))).replace(' ', '')))
    font = {'family': 'Microsoft Yahei'}
    matplotlib.rc("font", **font)
    plt.figure(figsize=(20, 40), dpi=80)
    plt.barh(range(len(name)), num, tick_label=name)
    plt.show()
