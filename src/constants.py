from collections import OrderedDict

# Map that defines any specially escaped punctuation.
# The keys are regular expressions and the values are the replacement string
PUNCTUATION_MAP = OrderedDict([
  ('\?', 'Q_MARK'),
  ('!', 'EXCLAIM'),
])

# Map that escapes any links
# The keys are regular expressions and the values are the replacement string
LINK_MAP = OrderedDict([
  ('https?:\/\/[^\s]+', 'LINK')
])

# Map that escapes usernames and hashtags
# The keys are regular expressions and the values are the replacement string
TWITTER_MAP = OrderedDict([
  ('(?:^|")@\w+', 'USERNAME'),
  ('(?:^|")#\w+', 'HASHTAG')
])

#partial date regexes
DAY_RE = '(?:sun(?:day)?|mon(?:day)?|tues(?:day)?|wed(?:nesday)?|thurs(?:day)?|fri(?:day)?|sat(?:urday)?)'
MONTH_RE = '(?:jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|jun(?:e)?|jul(?:y)?|aug(?:ust)?|sept(?:ember)|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)'
DAY_AND_YEAR_RE = '(?:,|, | )\d{1,2}(?:st|nd|rd|th)?(?:(?:,|, | )(?:\d{4}))?'
DATE_MAP = OrderedDict([
  #More descriptive dates eg. 12th of February, 15 august
  ('\d{{1,2}}(?:st|nd|rd|th)? (?:of )?{}'.format(MONTH_RE), 'DATE'),
  #textual date formats (february 15th, 2015, feb 15th, monday feb, 15th)
  ('{}?\s+{}{}'.format(DAY_RE, MONTH_RE, DAY_AND_YEAR_RE), 'DATE'),
  #number format dates "DD/MM/YYYY" or "DD/MM/YY" or "DD-MM-YY" or "DD-MM-YYYY"
  ('\d{1,2}[-|\/]\d{1,2}[-|\/]\d{2,4}', 'DATE'),
  #various other formats
  ('{} \d{{1,2}}\/\d{{1,2}}'.format(DAY_RE), 'DATE')
])

TIME_MAP = OrderedDict([
  ('\d{1,2}(?:(?:(?::\d{1,2}) ?(?:pm|am))|(?::\d{1,2})|(?: ?(?:pm|am)))', 'TIME')
])

LEFTOVER_DIGITS_MAP = OrderedDict([
  ('\d+(?:st|nd|rd|th)?', 'NUMBER')
])

LEFTOVER_PUNCTUATION_MAP = OrderedDict([
  ('\/|\\|\(|\)|#|\$|@|&|\*|"|<|>|\'|\]|\[|\{|\}', ''),
  ('--+', '')
])

def get_all_replacement_dicts():
  all_dicts = OrderedDict([])
  all_dicts.update(LINK_MAP)
  all_dicts.update(PUNCTUATION_MAP)
  all_dicts.update(TWITTER_MAP)
  all_dicts.update(TIME_MAP)
  all_dicts.update(DATE_MAP)
  all_dicts.update(LEFTOVER_DIGITS_MAP)
  all_dicts.update(LEFTOVER_PUNCTUATION_MAP)
  return all_dicts

# The possible mood strings
MOODS = ['positive', 'negative', 'neutral', 'objective']

# The character sequence to be used around any special replacements
ESCAPE_SEQUENCE = "%%"

# The basic tokenizing split regex
SPLIT_REGEX = ' |\n|\t|;|:|,|\.|\"'

#Header comment text
HEADER = """%
% CSI 4107
% Assignment 2 .arff file
% April 2, 2015
% Sean Billings\t6426637
% Craig Bryan\t6965144
%
% Generated from "semeval_twitter_data.txt"
"""
