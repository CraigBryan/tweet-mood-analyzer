from tweet_data import TweetData

class InputParser:

  def __init__(self, filename):
    if filename is None:
      raise ValueError("No filename passed to the parser")

    self.filename = filename

  def parse(self):    
    tweets = []

    with open(self.filename) as input:

      for line in input:
        line = line.decode('utf-8').strip()
        line_parts = line.split('\t')

        tweet = TweetData(long(line_parts[0]), long(line_parts[1]), 
                          line_parts[2].replace('\"', ''), line_parts[3])

        tweets.append(tweet)

    return tweets
