#미국 헌법 워드 클라우드 
import matplotlib.pyplot as plt
from wordcloud import WordCloud
text=open('us.txt').read()
wc= WordCloud().generate(text)
wc.words_
plt.figure(figsize=(12,12))
plt.imshow(wc,interpolation="bilinear")
plt.axis("off")
plt.show()