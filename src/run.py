import sys
from input_parser import InputParser
from  simple_filters import Analyzer
import constants
from feature import Feature
from arff_generator import DogSoundFileGenerator

options = []

if len(sys.argv) > 1:
  options = sys.argv[1:]

if '-t' in options:
  filename = '../res/one_tenth_semeval_twitter_data.txt'
else:
  filename = '../res/semeval_twitter_data.txt'

parser = InputParser(filename)
tweet_list = parser.parse()

analyzer = Analyzer(constants.ESCAPE_SEQUENCE)

for data in tweet_list:
 print(analyzer.analyze(data.tweet_string))

# EXAMPLE USE OF A FEATURE
# This example just uses the basic data contained in the tweet, but shows
# how the features and outputter are meant to be used

# features = []
# features.append(Feature("id", "numeric", "sid"))
# features.append(Feature("uid", "numeric", "uid"))
# features.append(Feature("mood", "enum", "mood", enum_fields = constants.MOODS))
# features.append(Feature("tweet_string", "string", "get_quoted_tweet_string"))

# output_gen = DogSoundFileGenerator("tweet_mood", tweet_list)

# output_gen.add_to_features(features)

# output_gen.generate_output("../res/test_output.arff")