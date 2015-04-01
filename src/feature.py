class Feature:
  """
  Defines a feature that works on the tweet data.
  """

  valid_types = [
    'numeric',
    'NUMERIC',
    'string',
    'STRING',
    #'date', #UNSUPPORTED
    #'DATE', #UNSUPPORTED
    'enum',
    'ENUM'
  ]

  def __init__(self, name, weka_type, data_identifier, 
               enum_fields = None, data_param = None):
    """
    Parameters:
      name - The name of the attribute
      weka_type - The type of the attribute, can be one of 'numeric', 'string',
                  'enum' (known as 'nominal-specification' in Weka), or date 
                  (date is currently unsupported)
      data_identifier - The string that a TweetData can respond to, which
                        will populate the data corresponding to the feature
      enum_fields - Only used for the 'enum' type, enumerates the options for 
                    that enum
      data_param - Used when data_identifier is called on a tweet as a
                   parameter. Only a single parameter for simplicity
    """
    self.name = name
    self.weka_type = weka_type
    self.data_identifier = data_identifier
    self.enum_values = enum_fields
    self.data_param = data_param

    #some unpythonic validation
    if self.weka_type not in Feature.valid_types:
      raise ValueError("Invalid type passed to feature")

  def __str__(self):
    if self.weka_type == 'enum':
      type_string = "{{{}}}".format(','.join(self.enum_values).encode('utf-8'))
    else:
      type_string = self.weka_type

    return "@ATTRIBUTE {} {}".format(self.name.encode('utf-8'), type_string)

  def apply_to_tweet(self, tweet):
    """
    This is where the feature is expecting the tweet to respond to the string
    in data_identifier. First, it attempts to call the tweet's response, then
    it just gives the value of 
    """

    tweet_field = getattr(tweet, self.data_identifier)

    try:
      if self.data_param is not None:
        data = tweet_field(self.data_param)
      else:
        data = tweet_field()
    except TypeError: #This will happen if tweet.data_identifier is not callable
      data = tweet_field

    #some unpythonic validation
    if self.weka_type in ['enum', 'ENUM']:
      if data not in self.enum_values:
        raise ValueError("Weka enum type not a defined type")
    
    return data