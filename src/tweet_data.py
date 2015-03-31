class TweetData:

  def __init__(self, aSid, aUid, aMood, aTweet, tokens = None, pos_score = 0, neg_score = 0, obj_score = 0, qMarks = 0, eMarks = 0):
    self.sid = aSid
    self.uid = aUid
    self.mood = aMood
    self.tweet_string = aTweet
    self.pos_score = pos_score
    self.neg_score = neg_score
    self.obj_score = obj_score
    self.qMarks = qMarks
    self.eMarks = eMarks
    
    

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

  def count_exclamation_and_question_marks(self, tokens):

    for word in tokens:
      if word == '%%Q_MARK%%':
        self.qMarks += 1
      if word =='EXCLAIM%%':
        self.eMarks += 1
