import sys
from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud

d = path.dirname(__file__)

text = open(sys.argv[1]).read()
wordcloud = WordCloud().generate(text)
img = plt.imshow(wordcloud)
plt.axis("off")
plt.show()

img.write_png("wordcloud_password.png")
