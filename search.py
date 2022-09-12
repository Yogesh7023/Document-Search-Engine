import pandas as pd
from rank_bm25 import *
import warnings
warnings.filterwarnings('ignore')
import nltk
from nltk.tokenize import word_tokenize
sentence = "Jack is a sharp minded fellow"
words = word_tokenize(sentence)
print(words)

def spl_chars_removal(lst):
    lst1=list()
    for element in lst:
        str=""
        str = re.sub("[0-9a-zA-Z]"," ",element)
        lst1.append(str)
    return lst1
  
  #adding words to stopwords
from nltk.tokenize import word_tokenize
from gensim.parsing.preprocessing import STOPWORDS

#adding custom words to the pre-defined stop words list
all_stopwords_gensim = STOPWORDS.union(set(['disease']))

def stopwprds_removal_gensim_custom(lst):
    lst1=list()
    for str in lst:
        text_tokens = word_tokenize(str)
        tokens_without_sw = [word for word in text_tokens if not word in all_stopwords_gensim]
        str_t = " ".join(tokens_without_sw)
        lst1.append(str_t)
 
    return lst1

import nltk
from nltk.stem import PorterStemmer
ps = PorterStemmer() 
sentence = "Machine Learning is cool"
for word in sentence.split():
    print(ps.stem(word))
    
lst1=open('D:\document search/Dictionary1.txt')
lst2=spl_chars_removal(lst1)
lst=stopwprds_removal_gensim_custom(lst2)
search=1
while search>0:
    b = input("Search keywords? (y/n)\n")
    if (b == 'y'):
        query = input("Enter the search string : ")
        tokenized_query = query.split(" ")
        tokenized_corpus = [doc.split(" ") for doc in lst]
        bm25 = BM25Okapi(tokenized_corpus)
        doc_scores = bm25.get_scores(tokenized_query)
        print(doc_scores)
    elif (b == 'n'):
        search=0
