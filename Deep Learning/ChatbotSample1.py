from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

'''
Bag Of Words method
'''
simple_train=['call you tonight','call me a cab','please call me','call me later']
vect=CountVectorizer()
vect.fit(simple_train)
vect.get_feature_names()
print(vect.get_feature_names())

simple_train_dtm = vect.transform(simple_train)
#print(simple_train_dtm)
simple_train_dtm.toarray()
print(simple_train_dtm.toarray())
print(pd.DataFrame(simple_train_dtm.toarray(), columns=vect.get_feature_names()))
