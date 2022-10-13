import matplotlib
import requests
import re
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

if __name__ == '__main__':
    # url = 'https://tenapi.cn/resou/'
    # # 发送请求
    # response = requests.get(url=url)
    # # 去除最外层的嵌套
    # data = response.json()["list"][:]
    # name = []
    # num = []
    # black = []
    # # 标记部分没有热度数值的数据
    # for i in range(len(data)):
    #     if data[i]['hot'] == '':
    #         black.append(i)
    # for i in range(len(data)):
    #     if i not in black:
    #         # 如果有热度数，就加入图标
    #         name.append(data[i]['name'])
    #         # 有的热度数有分区，去分区信息
    #         num.append(int((re.sub('[\u4e00-\u9fa5]', '', str(data[i]['hot']))).replace(' ', '')))
    header = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Mobile Safari/537.36',
        'Host': 's.weibo.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Cookie': 'SUB=_2AkMUGjsrf8NxqwFRmP0TxGLlbI1-zwnEieKiRsrwJRMxHRl-yT92qhNetRB6P5oVxEApmv1xh3frvIztW2F0Z8WEgysT; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5Kj9z8xsxhPlHcf74GnrC3; _s_tentry=-; Apache=4848537682237.713.1665666917789; SINAGLOBAL=4848537682237.713.1665666917789; ULV=1665666917807:1:1:1:4848537682237.713.1665666917789:'
    }
    # 发送请求并接收响应内容
    res = requests.get('https://s.weibo.com/top/summary?cate=realtimehot', headers=header)
    # 获取热搜榜的内容
    items = BeautifulSoup(res.text, 'html.parser').find('section', {'class': 'list'})
    result = {}
    for li in items.find_all('li'):
        # 提取span标签内，em标签外的内容
        content = re.sub('<span.*?>', '', str(li.find('span'))).split('<em>')[0]
        # 提取em标签内的内容
        num = re.findall(r'<em>(.*?)</em>', str(li.find('span')))
        # 将内容存入字典
        if num not in [[''], []]:
            result[content] = int(num[0])
    # 设置字体
    font = {'family': 'Microsoft Yahei'}
    matplotlib.rc("font", **font)
    plt.figure(figsize=(20, 40), dpi=160)
    plt.barh(range(len(list(result.keys()))), list(result.values()), tick_label=list(result.keys()))
    # 设置数据显示
    plt.bar_label(plt.gca().containers[0])
    plt.show()
