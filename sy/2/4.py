import wordcloud
import matplotlib.pyplot as plt

xz = open("C:/Users/93601/Code/python/sy/2/校长2018.txt", "r", encoding='utf-8').read()
xzby = open("C:/Users/93601/Code/python/sy/2/校长2018毕业讲话.txt", "r", encoding='utf-8').read()

w1 = wordcloud.WordCloud(width=1000, height=700, background_color="white", font_path="msyh.ttc").generate(xz)
w2 = wordcloud.WordCloud(width=1000, height=700, background_color="white", font_path="msyh.ttc").generate(xzby)

plt.imshow(w1)
plt.axis("off")
plt.show()

plt.imshow(w2)
plt.axis("off")
plt.show()
