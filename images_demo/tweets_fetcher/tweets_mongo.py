import mongoengine

class TweetMongo(mongoengine.Document):
    '''
    Model of twitter tweet.
    '''
    tweet_id = mongoengine.StringField(required=True, unique=True)
    tweet_data = mongoengine.DynamicField(required=True)


def connect():
    '''
    '''
    return mongoengine.connect('test', host='mongo', port=27017)

def saveTweets(list_of_twitts=None):
    print 'Save tweets'
    for tweet in list_of_twitts:
        try:
            tweet_mongo = TweetMongo(tweet_id = str(tweet['id']),
                                          tweet_data = tweet)
            tweet_mongo.save()
        except Exception as e:
            print e.message
            pass
