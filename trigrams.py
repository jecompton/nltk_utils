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

# trigram libs
from nltk.collocations import *

text = 'Mary had a little lamb. Her fleece was white as snow'

if len(sys.argv) > 1:
  with codecs.open(sys.argv[1], "r", encoding='utf8') as f:
    text = f.read()

#print(stoplist)

def build_trigrams(stoplist):
  words = [word for word in word_tokenize(text) if word not in stoplist]

  trigram_measures = nltk.collocations.TrigramAssocMeasures()
  finder = TrigramCollocationFinder.from_words(words)
  trigramlist = sorted(finder.ngram_fd.items())
  trigramlist.sort(key=lambda item: item[-1], reverse=True)
  return trigramlist

trigram_list = build_trigrams(stoplist)
print('Top 10 trigrams with just punctuation filtered')
print(trigram_list[0:9])

stoplist.extend(stopwords.words('english'))
trigram_list = build_trigrams(stoplist)
print('Top 10 trigrams with common English words filtered out')
print(trigram_list[0:9])
