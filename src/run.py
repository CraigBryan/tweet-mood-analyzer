import sys
from input_parser import InputParser
from  simple_filters import Analyzer
import constants
from feature import Feature
from arff_generator import DogSoundFileGenerator
from unigram_swn_feature_parser import UnigramSWNFeatureParser
from bag_of_words_generator import BagOfWordsGenerator 

options = ['-t', '-swn', '-qe']

if len(sys.argv) > 1:
  options = sys.argv[1:]

if '-t' in options:
  filename = '../res/one_tenth_semeval_twitter_data.txt'
else:
  filename = '../res/semeval_twitter_data.txt'

parser = InputParser(filename)
tweet_list = parser.parse()

#All preprocessing necessary
print('Started preprocessing')

analyzer = Analyzer(constants.ESCAPE_SEQUENCE)
uFeatureParser = UnigramSWNFeatureParser()

for data in tweet_list:
  tokens = analyzer.analyze(data.tweet_string)

  for term in tokens:
    term = term.encode('utf_8').decode('ascii', 'ignore')
      
  data.set_tokens(tokens)
  data.set_scores(uFeatureParser.score(tokens))

print('Done Preprocessing')                  

# Adding features

features = []
# The words are now added as a bag of words instead
# features.append(Feature("tweet_string", "string", "tokens"))

if '-uid' in options:
  features.append(Feature("uid", "numeric", "uid"))

if '-cap' in options:
  features.append(Feature("caps", "numeric", "count_caps"))

if '-swn' in options:
  features.append(Feature("pos_score", "numeric", "pos_score"))
  features.append(Feature("neg_score", "numeric", "neg_score"))
  features.append(Feature("obj_score", "numeric", "obj_score"))

if '-qe' in options:
  features.append(Feature("q_marks", "numeric", "q_marks"))
  features.append(Feature("e_marks", "numeric", "e_marks")) 

if '-bow' in options:
  bow_generator = BagOfWordsGenerator(tweet_list)
  bow_generator.generate_bag_of_words()
  bow_generator.assign_word_vectors()
  features.extend(bow_generator.generate_word_features())


features.append(Feature("category", "enum", "mood", enum_fields = constants.MOODS))

# Outputting the arff

output_gen = DogSoundFileGenerator("tweet_mood", tweet_list)
output_gen.add_to_features(features)

output_gen.generate_output("../res/test_output.arff")