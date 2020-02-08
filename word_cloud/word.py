#%matplotlib inline

from konlpy.tag import Twitter 
from collections import Counter

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk 
from nltk.corpus import stopwords

import matplotlib 
from IPython.display import set_matplotlib_formats


if __name__ == '__main__':
    file = open("sample.txt", 'r')
    lists = file.readlines()
    file.close()
    #print(lists)
    twitter = Twitter()
    morphs = []
    for sentence in lists:
        morphs.append(twitter.pos(sentence))
        
    #print(morphs)
    noun_adj_adv_list=[]
    for sentences in morphs:
        for word, tag in sentences:
            if tag in ['Noun'] and ('것' not in word) and ("내" not in word)and ("나" not in word)and ("수"not in word) and("게"not in word)and("말"not in word):
                noun_adj_adv_list.append(word)
                
    #print(noun_adj_adv_list)
    count = Counter(noun_adj_adv_list)
    words = dict(count.most_common())
    #print(words)

    
    matplotlib.rc('font',family = 'Malgun Gothic') 
    set_matplotlib_formats('retina') 
    matplotlib.rc('axes',unicode_minus = False)

    wordcloud = WordCloud(font_path = 'malgun.ttf', background_color='white',colormap = "Accent_r", width=1500,             height=1000).generate_from_frequencies(words) 
    
    plt.imshow(wordcloud, interpolation='bilinear') 
    plt.axis('off') 
    plt.show()
    plt.savefig('word.png', bbox_inches='tight')
    
        


 



