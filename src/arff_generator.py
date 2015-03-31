import constants

class DogSoundFileGenerator:
  """
  Get it? This class generates arff files.
  """

  def __init__(self, name, tweet_data):
    self.name = name;
    self.tweets = tweet_data
    self.features = []

  def add_to_features(self, feature):
    self.features.extend(feature)

  def generate_output(self, filename):
    self._gen_header(filename)

    for feature in self.features:
      self._gen_feature_attribute_output(feature, filename)

    self._write_to_file(filename, "")
    self._gen_data_header(filename)

    for tweet in self.tweets:
      self._gen_tweet_data_row_output(filename, tweet)

  def _gen_header(self, filename):
    """
    Creates the header and erases overwrites any existing file
    """
    with open(filename, 'w') as output:
      line = constants.HEADER + "@RELATION tweet\n"
      output.write(line + "\n")

  def _gen_feature_attribute_output(self, feature, filename):
    self._write_to_file(filename, str(feature))

  def _gen_data_header(self, filename):
    self._write_to_file(filename, "@DATA")

  def _gen_tweet_data_row_output(self, filename, tweet):
    data = []
    for feature in self.features:
      try:
        data.append(str(feature.apply_to_tweet(tweet)))
      except UnicodeDecodeError:
        data.append(str(feature.apply_to_tweet(tweet).encode('utf-8')))

    self._write_to_file(filename, ','.join(data))

  def _write_to_file(self, filename, line):
    with open(filename, 'a+') as output:
      output.write(line + "\n")
