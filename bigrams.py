import sys
import codecs
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Stopwords to filter
from nltk.corpus import stopwords
from string import punctuation
#stoplist = set(stopwords.words('english') + list(punctuation))
stoplist = [x.decode('UTF8') for x in set(list(punctuation))]
# Other punctuation, i.e. left and right versions of quotes
stoplist.extend([u'\u201d', u'\u201c', u'\u2019', u'\u2014']) 

# bigram libs
from nltk.collocations import *

text = 'Mary had a little lamb. Her fleece was white as snow'

if len(sys.argv) > 1:
  with codecs.open(sys.argv[1], "r", encoding='utf8') as f:
    text = f.read()

#print(stoplist)

def build_bigrams(stoplist):
  words = [word for word in word_tokenize(text) if word not in stoplist]

  bigram_measures = nltk.collocations.BigramAssocMeasures()
  finder = BigramCollocationFinder.from_words(words)
  bigramlist = sorted(finder.ngram_fd.items())
  bigramlist.sort(key=lambda item: item[-1], reverse=True)
  return bigramlist

bigram_list = build_bigrams(stoplist)
print('Top 10 bigrams with just punctuation filtered')
print(bigram_list[0:9])

stoplist.extend(stopwords.words('english'))
bigram_list = build_bigrams(stoplist)
print('Top 10 bigrams with common English words filtered out')
print(bigram_list[0:9])
