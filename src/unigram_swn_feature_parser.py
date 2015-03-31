import nltk
from nltk.corpus import sentiwordnet as swn
from nltk.tokenize import word_tokenize
from tweet_data import TweetData

class UnigramSWNFeatureParser:


    def score(self, tokens):
        pos_value = 0.0
        neg_value = 0.0
        obj_value = 0.0
        
        #TODO disambiguation via POS tagging using nps_chat or Brown Corpus

        lengthOfData = 0
        for word in tokens:
            meanings = list(swn.senti_synsets(word))
            
            if len(meanings) > 0:
                wordSynset0 = meanings[0]
                pos_value += wordSynset0.pos_score()
                neg_value += wordSynset0.neg_score()
                obj_value += wordSynset0.obj_score()
                lengthOfData += 1
                
        if lengthOfData > 0:
            pos_value = pos_value
            neg_value = neg_value
            obj_value = obj_value/lengthOfData

        return [ pos_value , neg_value, obj_value]
    

    def generateARFF(self, filename):
        f = open(filename, 'w')
        f.write("@relation opinion \n")
        f.write("@attribute sentence string \n")
        f.write("@attribute posScore numeric \n")
        f.write("@attribute negScore numeric \n")
        f.write("@attribute objScore numeric \n")
        f.write("@attribute category {positive, negative, neutral, objective} \n")
        f.write("@data")

        for tweet in self.tweets:
            scores = self.score(tweet)
            f.write("' %s , %s , %s , %s , %s \n" \
                    %(tweet.tweetString, scores[0], scores[1], scores[2],  tweet.mood) )
        
            
