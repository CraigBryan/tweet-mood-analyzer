class TweetData:

  mood_strings = ['"positive"', '"negative"', '"neutral"', '"objective"']

  def __init__(self, aSid, aUid, aMood, aTweet):
    self.sid = aSid
    self.uid = aUid
    self.mood = aMood
    self.tweetString = aTweet

  @property
  def mood(self):
    return self._mood

  @mood.setter
  def mood(self, value):
    if not value in mood_strings:
      raise ValueError("%s is not a valid mood")
    
    self._mood = value

  def __str__(self):
    return "sid: %s \nuid: %s \nmood: %s \ntweet: %s" \
      %(self.sid, self.uid, self.mood, self.tweetString)