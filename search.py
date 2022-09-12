{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from rank_bm25 import *\n",
    "import warnings\n",
    "warnings.filterwarnings('ignore')\n",
    "import nltk\n",
    "from nltk.tokenize import word_tokenize\n",
    "sentence = \"Jack is a sharp minded fellow\"\n",
    "words = word_tokenize(sentence)\n",
    "print(words)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def spl_chars_removal(lst):\n",
    "    lst1=list()\n",
    "    for element in lst:\n",
    "        str=\"\"\n",
    "        str = re.sub(\"[0-9a-zA-Z]\",\" \",element)\n",
    "        lst1.append(str)\n",
    "    return lst1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "#adding words to stopwords\n",
    "from nltk.tokenize import word_tokenize\n",
    "from gensim.parsing.preprocessing import STOPWORDS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "#adding custom words to the pre-defined stop words list\n",
    "all_stopwords_gensim = STOPWORDS.union(set(['disease']))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "def stopwprds_removal_gensim_custom(lst):\n",
    "    lst1=list()\n",
    "    for str in lst:\n",
    "        text_tokens = word_tokenize(str)\n",
    "        tokens_without_sw = [word for word in text_tokens if not word in all_stopwords_gensim]\n",
    "        str_t = \" \".join(tokens_without_sw)\n",
    "        lst1.append(str_t)\n",
    " \n",
    "    return lst1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "machin\n",
      "learn\n",
      "is\n",
      "cool\n"
     ]
    }
   ],
   "source": [
    "import nltk\n",
    "from nltk.stem import PorterStemmer\n",
    "ps = PorterStemmer() \n",
    "sentence = \"Machine Learning is cool\"\n",
    "for word in sentence.split():\n",
    "    print(ps.stem(word))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "search=1\n",
    "while search>0:\n",
    "    b = input(\"Search keywords? (y/n)\\n\")\n",
    "    if (b == 'y'):\n",
    "        query = input(\"Enter the search string : \")\n",
    "        tokenized_query = query.split(\" \")\n",
    "        lst1=open('D:\\document search/Dictionary.txt')\n",
    "        tokenized_corpus = [doc.split(\" \") for doc in lst1]\n",
    "        bm25 = BM25Okapi(tokenized_corpus)\n",
    "        doc_scores = bm25.get_scores(tokenized_query)\n",
    "        print(doc_scores)\n",
    "    elif (b == 'n'):\n",
    "        quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
