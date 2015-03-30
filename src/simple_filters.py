from collections import OrderedDict
from nltk.corpus import stopwords 
from nltk import word_tokenize
from nltk.stem import PorterStemmer
import string
import re

class Tokenizer:

  def tokenize(self, data):
    return word_tokenize(data)

class StopWordRemover:
  
  def __init__(self):
    self._stopWordSet = set(stopwords.words('english'))

  def filter(self, data):
    try:
      data = data.split(" ")
    except AttributeError:
      pass

    for word in data:
      if word in self._stopWordSet:
        data.remove(word)

    return data


class PunctuationFilterer:

  #order matters
  punctuation_map = OrderedDict([
    ('\?', 'Q_MARK%'),
    ('\?\?', 'DOUBLE_Q_MARK'),
    ('\?\?\?+', 'MULTI_Q_MARK'),
    ('!', 'EXCLAIM'),
    ('!!', 'DOUBLE_EXCLAIM'),
    ('!!!+', 'MULTI_EXCLAIM'),
    ('[\?|!]*[\?!|!\?]+[\?|!]*', 'EXCLAIM_QMARK_MIX')
  ])

  def __init__(self):
    self.exclusion = set(string.punctuation)

  def simple_filter(self, data):
    try:
      data = data.split(" ")
    except AttributeError:
      pass

    return [word for word in data if word not in self.exclusion]

  def replace_and_filter(self, data):
    try:
      data = data.split(" ")
    except AttributeError:
      pass

    for index, word in enumerate(data):
      temp_word = word
      for pattern, result in PunctuationFilterer.punctuation_map.items():
        if re.search(pattern, word):
          temp_word = result
      data[index] = temp_word

    return self.simple_filter(data)

class Stemmer(PorterStemmer):

  #allows us to stop stemming on patterns, such as punctuation replacements
  ignore_patterns = set([])

  def stem(self, data):
    for word in data:
      if word not in Stemmer.ignore_patterns:
        return super(Stemmer, self).stem(word)
      else:
        return word