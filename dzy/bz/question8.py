import requests
from bs4 import BeautifulSoup
import re
import time
import matplotlib.pyplot as plt

# 定义请求头
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42',
    'Host': 's.weibo.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cookie': 'SUB=_2AkMUGjsrf8NxqwFRmP0TxGLlbI1-zwnEieKiRsrwJRMxHRl-yT92qhNetRB6P5oVxEApmv1xh3frvIztW2F0Z8WEgysT; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5Kj9z8xsxhPlHcf74GnrC3; WBPSESS=lGn6cRy34B6AsqM-wzgd2HCTMpCo042RM9Fb3pmKiLUvSDY6_D7pMIoC_BlzVJQuthStDJLZzCCMrr5jmCjwnh3vS2Cg4j6IzeuE1Ma9hvPj5qu1gP2likat4BkHCgPVDTky-vqqLD9wG2bb-2q3CiWqP_IvpI_Vrp33tW6QoEE=; XSRF-TOKEN=1iRm25fcCwOHa4fcGi8FKRxh'
}
# 设置请求连接
url = 'https://s.weibo.com/top/summary?cate=realtimehot'
# 发送请求并接收响应内容
res = requests.get(url, headers=header)
# 获取热搜榜的内容
soup = BeautifulSoup(res.text, 'html.parser')
items = soup.find('section', {'class': 'list'})
result = {}
for li in items.find_all('li'):
    span = str(li.find('span'))
    # 提取span标签内，em标签外的内容
    content = re.sub('<span.*?>', '', span)
    content = content.split('<em>')[0]
    # 提取em标签内的内容
    num = re.findall(r'<em>(.*?)</em>', span)
    # 将内容存入字典
    if not num in [[''], []]:
        result[content] = int(num[0])
# 字典转换为列表
_result = result
result = list(result.items())
# 删除置顶的一条数据
result.pop(0)
# 获取当前时间
now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
# 保存到csv文件中
with open('weibo.csv', 'w', encoding='utf-8') as f:
    f.write('数据获取时间：' + now + '\n')
    f.write('热搜内容,热度\n')
    # 热搜排名
    id = 1
    # 遍历结果
    for key, value in result:
        f.write(str(id) + ',' + key + ',' + str(value) + '\n')
        id += 1
# 根据热度绘制柱状图
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 设置图片大小
plt.figure(figsize=(30, 30), dpi=80)
# 设置标题
plt.title('微博热搜榜')
# 设置x轴标签
plt.xlabel('热度')
x = list(_result.values())
y = list(_result.keys())
# 绘制柱状图
bar = plt.barh(range(len(y)), x, tick_label=y)
plt.bar_label(bar, padding=3)
# 显示图片
plt.show()
