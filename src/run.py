import sys
from input_parser import InputParser
from  simple_filters import Analyzer
import constants
from feature import Feature
from arff_generator import DogSoundFileGenerator
from unigram_swn_feature_parser import UnigramSWNFeatureParser
from bag_of_words_generator import BagOfWordsGenerator 

available_options = ['-swn', '-qe', '-uid', '-cap', '-bow', '-r', '-rt', '-emoji']

if len(sys.argv) > 1:
  options = sys.argv[1:]

if '-t' in options:
  filename = '../res/one_tenth_semeval_twitter_data.txt'
else:
  filename = '../res/semeval_twitter_data.txt'

if '-a' in options:
  options = available_options

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

if '-emoji' in options:
  features.append(Feature("pos_emoji", "numeric", "pos_emoticons"))
  features.append(Feature("neg_emoji", "numeric", "neg_emoticons")) 
  
if '-r' in options:
  features.append(Feature("is_reply", "enum", 
                          "is_reply", enum_fields = ['True', 'False']))

if '-rt' in options:
  features.append(Feature("is_retweet", "enum", 
                          "is_retweet", enum_fields = ['True', 'False']))

features.append(Feature("category", "enum", 
                        "mood", enum_fields = constants.MOODS))

# Outputting the arff

output_gen = DogSoundFileGenerator("tweet_mood", tweet_list)
output_gen.add_to_features(features)

output_gen.generate_output("../res/test_output.arff")

print("Output Successful")

if '-info' in options:
  replies = 0
  retweets = 0
  for tweet in tweet_list:
    if tweet.is_reply() == 'True':
      replies += 1
    if tweet.is_retweet() == 'True':
      retweets += 1

  print("Number of hashtags found: {}".format(bow_generator.corpus.word_count_dictionary['HASHTAG']))
  print("Number of usernames found: {}".format(bow_generator.corpus.word_count_dictionary['USERNAME']))
  print("Number of exclamation marks found: {}".format(bow_generator.corpus.word_count_dictionary['EXCLAIM']))
  print("Number of question marks found: {}".format(bow_generator.corpus.word_count_dictionary['Q_MARK']))
  print("Number of links found: {}".format(bow_generator.corpus.word_count_dictionary['LINK']))
  print("Number of dates found: {}".format(bow_generator.corpus.word_count_dictionary['DATE']))
  print("Number of times found: {}".format(bow_generator.corpus.word_count_dictionary['TIME']))
  print("Number of numbers found: {}".format(bow_generator.corpus.word_count_dictionary['NUMBER']))
  print("Number of replies: {}".format(replies))
  print("Number of retweets: {}".format(retweets))