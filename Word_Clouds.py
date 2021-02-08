import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image
import io

with io.open('text.txt', 'r', encoding='utf-16le') as f:
    data = f.read()


def buzz_word(string):
    mask_arr = np.array(Image.open("Brain_2.jpeg"))
    cloud = WordCloud(background_color="white",
                      max_words=200, mask=mask_arr,
                      stopwords=set(STOPWORDS))
    cloud.generate(string)
    cloud.to_file("WordCloud.jpeg")


data = data.lower()
buzz_word(data)
