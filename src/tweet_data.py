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
    return '"{}"'.format(self.tweet_string.encode('utf-8'))