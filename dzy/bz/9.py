import re
import wordcloud
import jieba
import matplotlib.pyplot as plt

if __name__ == '__main__':
    with open('C:/Users/93601/Code/python/dzy/bz/水浒传.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    _text = text
    # 替换标点
    text = re.sub('\W*', '', text)
    # 分词
    cutted = list(jieba.cut(text))
    count = {}
    # 计数
    for i in cutted:
        if len(i) == 1:
            continue
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    # 排序
    sort = sorted(count.items(), key=lambda x: x[1], reverse=True)
    print(sort[:10])
    w1 = wordcloud.WordCloud(width=1000, height=700, background_color="white", font_path="msyh.ttc").generate(_text)
    plt.imshow(w1)
    plt.axis("off")
    plt.show()
