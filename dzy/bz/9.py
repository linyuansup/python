import re

import jieba

if __name__ == '__main__':
    with open('C:/Users/93601/Code/python/dzy/bz/水浒传.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    text = re.sub('\W*', '', text)
    cutted = list(jieba.cut(text))
    count = {}
    for i in cutted:
        if len(i) == 1:
            continue
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    sort = sorted(count.items(), key=lambda x: x[1], reverse=True)
    print(sort[:10])
