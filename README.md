# nltk\_utils

This is a grab bag of scripts intended to help in using nltk for certain tasks,
with a focus on using them as interactive command line utlities.

The word_freq.py script, for example, has a number of commandline options and
expects a text file. It then gives you a frequency statistics report for most
common words. You can easily filter out stopwords, punctuation, and tune your
investigation as you like.

This is useful for exploring the text and finding directions you might go with
an ML algorithm such as a classifier. It can also help you find places in the
text that might contain dirty data, such as unusual punctuation characters that
aren't filtering out.

You can get a lot of interesting results just by looking at bigrams and trigrams
for texts such as political speeches (but don't jump to conclusions--NLP of this
sort is a very inexact science).
