import sys
from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud

d = path.dirname(__file__)

text = open(sys.argv[1]).read()
wordcloud = WordCloud(max_font_size=40, relative_scaling=.5).generate(text)
img = plt.imshow(wordcloud)
plt.axis("off")
#plt.show()
plt.savefig("wordcloud_password.png")
