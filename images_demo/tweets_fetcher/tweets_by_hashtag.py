from twitter import Twitter, OAuth
from pprint import pprint
from datetime import datetime
import tweets_mongo
import time
import os

TW_ACCESS_TOKEN = os.getenv('TW_ACCESS_TOKEN', None)
TW_ACCESS_SECRET = os.getenv('TW_ACCESS_SECRET', None)
TW_CONSUMER_KEY = os.getenv('TW_CONSUMER_KEY', None)
TW_CONSUMER_SECRET = os.getenv('TW_CONSUMER_SECRET', None)


def fetchTrumpTweets():
    oauth = OAuth(TW_ACCESS_TOKEN, TW_ACCESS_SECRET, TW_CONSUMER_KEY, TW_CONSUMER_SECRET)
    twitter = Twitter(auth=oauth)
    query = twitter.search.tweets(q='#trump')

    #pprint(query)
    print('Connect to mongo')
    tweets_mongo.connect()
    print('Save ' + str(len(query['statuses'])) + ' tweets')
    tweets_mongo.saveTweets(query['statuses'])


if __name__ == '__main__':
    print 'Start tweets_fetcher by tags'

    counter = 1
    while True:
        fetchTrumpTweets()
        print 'Fetch counter ' + str(counter)
        print 'Wait 1080 seconds'
        time.sleep(1080)
        counter += 1
