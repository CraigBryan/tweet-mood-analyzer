import sys
from input_parser import InputParser
import simple_filters

options = []

if len(sys.argv) > 1:
  options = sys.argv[1:]

if '-t' in options:
  filename = '../res/one_tenth_semeval_twitter_data.txt'
else:
  filename = '../res/semeval_twitter_data.txt'

parser = InputParser(filename)
tweetList = parser.parse()

#Do things with tweetList
data = tweetList[0].tweetString

print("Before tokenization: %s" % data)

tokenizer = simple_filters.Tokenizer()
t_data = tokenizer.tokenize(data)

print("After tokenization: %s" % t_data)

print("Before stopword removal: %s" % t_data)

sw_filter = simple_filters.StopWordRemover()
sw_data = sw_filter.filter(t_data)

print("After stopword removal: %s" % sw_data)

print("Before punctuation filtering: %s" % sw_data)

punct_filter = simple_filters.PunctuationFilterer()
p_data = punct_filter.simple_filter(sw_data)
pr_data = punct_filter.replace_and_filter(sw_data)

print("After simple punctuation filtering: %s" % p_data)
print("After replace and filtering: %s" % pr_data)

print("Before stemming (non-replaced): %s" % p_data)

stemmer = simple_filters.Stemmer()
st_data = stemmer.stem(p_data)

print("After stemming (non-replaced): %s" % st_data)

print("Before stemming (replaced): %s" % pr_data)

str_data = stemmer.stem(pr_data)

print("After stemming (replaced): %s" % str_data)