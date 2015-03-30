import sys
from input_parser import InputParser
from  simple_filters import Analyzer
import constants

options = []

if len(sys.argv) > 1:
  options = sys.argv[1:]

if '-t' in options:
  filename = '../res/one_tenth_semeval_twitter_data.txt'
else:
  filename = '../res/semeval_twitter_data.txt'

parser = InputParser(filename)
tweetList = parser.parse()

analyzer = Analyzer(constants.ESCAPE_SEQUENCE)

for data in tweetList:
  print(analyzer.analyze(data.tweetString))