import matplotlib
import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

if __name__ == '__main__':
    header = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Mobile Safari/537.36',
        'Host': 's.weibo.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Cookie': 'SUB=_2AkMUGjsrf8NxqwFRmP0TxGLlbI1-zwnEieKiRsrwJRMxHRl-yT92qhNetRB6P5oVxEApmv1xh3frvIztW2F0Z8WEgysT; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5Kj9z8xsxhPlHcf74GnrC3; _s_tentry=-; Apache=4848537682237.713.1665666917789; SINAGLOBAL=4848537682237.713.1665666917789; ULV=1665666917807:1:1:1:4848537682237.713.1665666917789:'
    }
    # 发送请求
    response = requests.get('https://s.weibo.com/top/summary?cate=realtimehot', headers=header)
    # 获取数据
    items = BeautifulSoup(response.text, 'html.parser').find('section', {'class': 'list'})
    res = {}
    for item in items.find_all('li'):
        span = str(item.find('span'))[6:].split('<')[0]  # 热度内容
        index = str(item.find('span')).find('<em>')  # 热度
        if not index == -1:  # 防止热度标签为空
            hot = str(item.find('span'))[index + 4:].split('<')[0]  # 截取热度字符串
            if not hot == '':  # 防止热度字符串为空
                res[span] = int(hot)  # 转型并插入
    # 设置字体
    font = {'family': 'Microsoft Yahei'}
    matplotlib.rc("font", **font)
    # 设置图片大小
    plt.figure(figsize=(20, 40), dpi=160)
    # 设置图表类型和数据
    plt.barh(range(len(list(res.keys()))), list(res.values()), tick_label=list(res.keys()))
    # 设置数据显示
    plt.bar_label(plt.gca().containers[0])
    plt.show()
