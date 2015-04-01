class TweetData:

  def __init__(self, aSid, aUid, aMood, aTweet):
    self.sid = aSid
    self.uid = aUid
    self.mood = aMood
    self.tweet_string = aTweet    

  def __str__(self):
    return "sid: %s \nuid: %s \nmood: %s \ntweet: %s" \
      %(self.sid, self.uid, self.mood, self.tweet_string)


  def get_quoted_tweet_string(self):
    return '\' {} \''.format(self.tweet_string.replace('\''," ").encode('utf-8'))

  def set_scores(self, scores):
    self.pos_score = scores[0]
    self.neg_score = scores[1]
    self.obj_score = scores[2]

  def set_tokens(self, tokens):
    self.tokens = tokens

  def q_marks(self):
    count = 0
    for word in self.tokens:
      if word == '%%Q_MARK%%':
        count += 1

    return count

  def e_marks(self):
    count = 0
    for word in self.tokens:
      if word == '%%EXCLAIM%%':
        count += 1
        
    return count

  def set_word_vector(self, vector):
    self.word_vector = vector

  def get_word_count(self, index):
    return self.word_vector[index]

  def count_caps(self):
    return sum(1 for c in self.tweet_string if c.isupper())

  def is_reply(self):
    return str(self.tokens[0] == 'USERNAME')

  def is_retweet(self):
    return str('rt' in self.tokens)