from flask import Flask
import mongoengine
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)

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


@app.route('/')
def hello_world():
    print connect()
    tweets_ids = unicode()
    for tweet in TweetMongo.objects:
        print tweet.tweet_id
        tweets_ids +=  str(tweet.tweet_data['text']) + '</br>'
    return tweets_ids

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
