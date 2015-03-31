import sys
from input_parser import InputParser
from  simple_filters import Analyzer
import constants
from feature import Feature
from arff_generator import DogSoundFileGenerator
from unigram_swn_feature_parser import UnigramSWNFeatureParser
import tweet_data

options = ['-t', '-swn', '-qe']

if len(sys.argv) > 1:
  options = sys.argv[1:]

if '-t' in options:
  filename = '../res/one_tenth_semeval_twitter_data.txt'
else:
  filename = '../res/semeval_twitter_data.txt'

parser = InputParser(filename)
tweet_list = parser.parse()

analyzer = Analyzer(constants.ESCAPE_SEQUENCE)

print('parsed \n')

uFeatureParser = UnigramSWNFeatureParser()

for data in tweet_list:
  tokens = analyzer.analyze(data.tweet_string)

  for term in tokens:
    term = term.encode('utf_8').decode('ascii', 'ignore')
      
  data.set_tokens(tokens)
  data.set_scores(uFeatureParser.score(tokens))
  data.count_exclamation_and_question_marks(tokens)

print('data updated')                  

# EXAMPLE USE OF A FEATURE
# This example just uses the basic data contained in the tweet, but shows
# how the features and outputter are meant to be used

features = []
features.append(Feature("tweet_string", "string", "tokens"))
if '-swn' in options:
  features.append(Feature("pos_score", "numeric", "pos_score"))
  features.append(Feature("neg_score", "numeric", "neg_score"))
  features.append(Feature("obj_score", "numeric", "obj_score"))

if '-qe' in options:
  features.append(Feature("q_marks", "numeric", "qMarks"))
  features.append(Feature("e_marks", "numeric", "eMarks")) 

features.append(Feature("category", "enum", "mood", enum_fields = constants.MOODS))


output_gen = DogSoundFileGenerator("tweet_mood", tweet_list)

output_gen.add_to_features(features)

output_gen.generate_output("../res/test_output.arff")
