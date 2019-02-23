import os
import pandas as pd
import nltk
import gensim
from gensim import corpora, models, similarities

'''
Window / Context way to convert words to vector
'''

#N-grams - usedsimilar as gensim
#Cosine

df=pd.read_csv('jokes.csv')
df.head()
df_x=df['Question'].values.tolist()
df_y=df['Answer'].values.tolist()
corpus=df_x+df_y
#print(df_x)
#print(df_y)
#print(corpus)

#list Comprehension
tkn_corp = [nltk.word_tokenize(sent) for sent in corpus]
#print(tkn_corp)


model = gensim.models.Word2Vec(tkn_corp, min_count=1, window=2, size=32)
model.save('testmodel')

model=gensim.models.Word2Vec.load('testmodel')

a1=model.wv.most_similar('American')
print(a1)

model.wv.similarity('man','woman')


