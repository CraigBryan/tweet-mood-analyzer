from collections import OrderedDict
from nltk.corpus import stopwords 
from nltk import word_tokenize
from nltk.stem import PorterStemmer
import string
import re

import constants

class Analyzer:
  """
  Combines the various filters and applies them to a given string
  """
  def __init__(self, seq):
    self._tokenizer = Tokenizer()
    self._sw_remover = StopWordRemover(set(stopwords.words('english')))
    self._punct_filter = PunctuationFilter(set(string.punctuation), seq)
    self._replacer = SpecialWordReplacer(constants.get_all_replacement_dicts(), 
                                        seq)
    self._stemmer = Stemmer(seq)

  def analyze(self, data):
    data = self._replacer.replace_special_sequences(data)
    data = self._tokenizer.tokenize(data)
    data = self._punct_filter.filter_apostrophes(data)
    data = self._sw_remover.filter(data)
    data = self._punct_filter.filter(data)
    data = self._stemmer.stem(data)
    data = self._remove_empty_words(data)
    return data

  def _remove_empty_words(self, data):
    return [word for word in data if not word == ""]

class Tokenizer:
  """
  Tokenizes a string
  """
  def tokenize(self, data):
    data = re.split(constants.SPLIT_REGEX, data)
    return data

class StopWordRemover:
  """
  Removes any stop words included in the passed-in stop word set
  """
  def __init__(self, stop_word_set):
    self._stop_word_set = stop_word_set

  def filter(self, data):
    try:
      data = data.split(" ")
    except AttributeError:
      pass

    for word in data:
      if word in self._stop_word_set:
        data.remove(word)

    return data

class PunctuationFilter:
  """
  Filters out any punctuation. To allow special sequences to exist, this filter
  will ignore any word surrounded by the passed-in special sequence
  """
  def __init__(self, punct_set, seq):
    self._exclusion = punct_set
    self._ignore_symbol = seq

  def filter(self, data):
    try:
      data = data.split(" ")
    except AttributeError:
      pass

    return [word for word in data if word not in self._exclusion] 

  def filter_apostrophes(self, data):
    try:
      data = data.split(" ")
    except AttributeError:
      pass

    for index, word in enumerate(data):
      data[index] = word.replace("'", "")

    return data

class SpecialWordReplacer:
  """
  Replaces any defined sequences so they can can be later ignored in the 
  preprocessing.
  """
  def __init__(self, replacement_dict, seq):
    self._replacement_dict = replacement_dict
    self._escape_seq = seq

  def replace_special_sequences(self, data):
    for pattern, result in self._replacement_dict.items():
      regex = re.compile(pattern)
      matches = regex.findall(data)
      for match in matches:
        data = data.replace(match, self._get_replacement(result))

    return data

  def _get_replacement(self, to_replace):
    return " " + self._escape_seq + to_replace + self._escape_seq + " "

class Stemmer(PorterStemmer):
  """
  Stems the words, ignoring any words started and ended with the escape sequence
  passed in.
  """
  def __init__(self, seq):
    super(Stemmer, self).__init__()
    self._escape_seq = seq

  def stem(self, data):
    try:
      data = data.split(" ")
    except AttributeError:
      pass

    for index, word in enumerate(data):
      if not re.search(self._escape_regex(), word):
        data[index] = super(Stemmer, self).stem(word)

    return data

  def _escape_regex(self):
    return '%s.+%s' %(self._escape_seq, self._escape_seq)