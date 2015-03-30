from collections import OrderedDict

# Map that defines any specially escaped punctuation.
# The keys are regular expressions and the values are the replacement string
# The order is important when dealing with repeated punctuation such as ? vs ???
PUNCTUATION_MAP = OrderedDict([
  ('\?', 'Q_MARK'),
  ('\?\?', 'DOUBLE_Q_MARK'),
  ('\?\?\?+', 'MULTI_Q_MARK'),
  ('!', 'EXCLAIM'),
  ('!!', 'DOUBLE_EXCLAIM'),
  ('!!!+', 'MULTI_EXCLAIM'),
  ('[\?|!]*[\?!|!\?]+[\?|!]*', 'EXCLAIM_QMARK_MIX')
])

# Map that escapes any links
# The keys are regular expressions and the values are the replacement string
LINK_MAP = OrderedDict([
  ('https?:\/\/[\w|\.|\/]+', 'LINK')
])

# Map that escapes usernames and hashtags
TWITTER_MAP = OrderedDict([
  ('@\w+', 'USERNAME'),
  ('#\w+', 'HASHTAG')
])

def get_all_replacement_dicts():
  all_dicts = OrderedDict([])
  all_dicts.update(PUNCTUATION_MAP)
  all_dicts.update(LINK_MAP)
  all_dicts.update(TWITTER_MAP)
  return all_dicts

# The character sequence to be used around any special replacements
ESCAPE_SEQUENCE = "%%"

# The basic tokenizing split regex
SPLIT_REGEX = ' |\n|\t|;|:|,|\.|\"'