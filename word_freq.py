#!/usr/bin/python

import argparse
import codecs
import nltk
from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import FreqDist
from string import punctuation
import sys

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Generate word frequency of a file')
  parser.add_argument('filename', metavar='FILE', nargs=1,
    help='Generate word frequency of a file')
  parser.add_argument('-e', '--stop-english', action='store_true', 
    help='Filter out common English words (e.g. \'a\', \'the\'')
  parser.add_argument('-n', '--num-words', metavar='N', type=int,
    default=20, action='store', 
    help='Choose how many words to desplay in the report table')
  parser.add_argument('--stem', action='store_true',
    help='Perform stemming on words (e.g. remove -ed, -ing from words)')
  parser.add_argument('-p', '--stop-punctuation', action='store_true',
    help='filter out punctuation')
  parser.add_argument('-u', '--preserve-uppercase', action='store_true',
    help='Preserve uppercase instead of downcasing')
  parser.add_argument('-w', '--words', metavar='WORD', nargs='+',
    help='One or more words of interest for extra stats')

  args = parser.parse_args()

  corpus_file = codecs.open(sys.argv[1], "r", encoding='utf8')

  try:
    text = corpus_file.read()
  finally:
    if corpus_file is not None:
      corpus_file.close()

  stoplist = []

  # Downcase by default since it tends to be more meaningful
  if not args.preserve_uppercase:
    print('here')
    text = text.lower()

  # First stash original data for stats
  orig_words = [word for word in word_tokenize(text) if word not in stoplist]
  orig_freq_dist = FreqDist(orig_words)

  if args.stop_english:
    stoplist +=  stopwords.words('english')
    #stoplist.append("'t")

  if args.stop_punctuation:
    stoplist +=  [x.decode('UTF8') for x in set(list(punctuation))]
    stoplist += [u'\u201d', u'\u201c', u'\u2019', u'\u2014']
    stoplist.append('--')

  words = [word for word in word_tokenize(text) if word not in stoplist]
  if args.stem:
    st = LancasterStemmer()
    words = [st.stem(word) for word in words]

  freq_dist = FreqDist(words)

  print('Total words: ' + str(orig_freq_dist.N()))
  print('Total after filter: ' + str(freq_dist.N()))
  # B() gives list of unique words
  print('Unique words: ' + str(freq_dist.B()))
  print('Unique words ratio: ' +str(float(freq_dist.B()) / float(freq_dist.N())))
  print('\n')

  if args.words:
    for word in args.words:
      print(word + ': ' + str(freq_dist[word]))
      print(word + ' freq: ' + str(freq_dist.freq(word)))
      print('\n')

  # Show top 30
  print('Top ' + str(args.num_words) + ' words:')
  freq_dist.tabulate(args.num_words)

