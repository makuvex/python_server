import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
from wordcloud import ImageColorGenerator


text = open('alice.txt').read()
'''
x, y = np.ogrid[:300, :300]

mask = (x - 150) ** 2 + (y - 150) ** 2 > 130 ** 2
mask = 255 * mask.astype(int)
'''

alice_mask = np.array(Image.open('a.png'))
image_colors = ImageColorGenerator(alice_mask)

wc = WordCloud(background_color='white', max_words=2000, mask=alice_mask, max_font_size=40, random_state=42)
wc.generate(text)
plt.figure(figsize=(12,12))

#plt.imshow(wc, interpolation="bilinear")
plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")
plt.show()
plt.savefig('singleword2.png', bbox_inches='tight')