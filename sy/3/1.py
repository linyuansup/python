import jieba

c = input("请输入一段文字：")
rev = jieba.cut(c)
rev = list(rev)
rev.reverse()
for i in rev:
    print(i, end="")
