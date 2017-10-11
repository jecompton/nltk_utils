import sys
import codecs
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

text = 'Mary had a little lamb. Her fleece was white as snow'

if len(sys.argv) > 1:
  with codecs.open(sys.argv[1], "r", encoding='utf8') as f:
    text = f.read()

sentences = sent_tokenize(text)
print('First sentence: ' + sentences[0])
print('Last sentence: ' + sentences[-1])
print('Number of sentences: ' + str(len(sentences)))
