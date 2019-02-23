import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

#nltk.download()

EXAMPLE_TEXT = "Hello, Guru. How are you Doing? Hope Python is easy. Do well. Work More"

print(sent_tokenize(EXAMPLE_TEXT))
print(word_tokenize(EXAMPLE_TEXT))

example_sent = "This is an sample. NLP sentence process ***** ^$^$^^%%^&%*& 0sdjsjdk "
stop_words = set(stopwords.words('english'))
print(type(stop_words))
stop_words.remove('is')
stop_words.add('a')
word_tkn = word_tokenize(example_sent)
filtered_sentence = []
for w in word_tkn:
    if w not in stop_words:
        filtered_sentence.append(w)

print(filtered_sentence)

ps = PorterStemmer()
new_text="It is duty of Programmer to Program. Programming will be good with more programs worked by programmer "
word = word_tokenize(new_text)
for w in word   :
    print(ps.stem(w))

limit = WordNetLemmatizer()

print('******************************************')
limit = WordNetLemmatizer()
for w in word:
    print(limit.lemmatize(w))

print(limit.lemmatize("better",pos='a'))
print(limit.lemmatize("catss"))
print(limit.lemmatize("cacti"))
print(limit.lemmatize("running"))
print(limit.lemmatize("run"))
print(limit.lemmatize("running",'v'))

syns = wordnet.synsets("program")
print(syns)

print(wordnet.synset('program.n.03').definition())
#list comprehension
print([str(lemma.name()) for lemma in wordnet.synset('program.n.01').lemmas()])

print(wordnet.sysnet('program.n.03').example()[0])
