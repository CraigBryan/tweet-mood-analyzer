from feature import Feature

class BagOfWordsGenerator:
  """
  Generates a global set of words and generates word vectors for each TweetData
  passed in.
  """

  def __init__(self, tweet_list):
    self.tweets = tweet_list
    self.corpus = TweetCorpus()
    self.corpus.wordCountDictionary = {}

  def generate_bag_of_words(self):
    for tweet in self.tweets:
      for word in tweet.tokens:
        self.corpus.add(word)

  def assign_word_vectors(self):
    for tweet in self.tweets:
      tweet.set_word_vector(self.corpus.generate_word_vector(tweet.tokens))

  def generate_word_features(self):
    word_features = []
    for index, word in enumerate(self.corpus.list()):
      if self.corpus.wordCountDictionary[word] > 5:
        word_features.append(Feature(word, 'numeric', 'get_word_count', 
                                   data_param = index))
    return word_features

class TweetCorpus:
  """
  Holds and uses the global set of words.
  """

  def __init__(self):
    self.word_set = set([])

  def add(self, word):
    if len(word) > 0:
      if word[0].isalpha():
        if word in self.word_set:
          self.wordCountDictionary[word] += 1
        else:
          self.wordCountDictionary[word] = 1
          self.word_set.add(word)
 #   else:
 #       print(word)
 #
 #  printed word was blannk in tests

  def generate_word_vector(self, tokens):
    word_vector = []
    for word in self.word_set:
      word_vector.append(tokens.count(word))

    return word_vector

  def list(self):
    return self.word_set
