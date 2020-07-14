import tweepy
import time

consumer_key = 'Z**B*************U***y'
consumer_secret = 'Z**B***********Z**B*************U***y********U***yc'
access_token = 'Z**B*************U***yZ**B*****Z**B*************U***y'
access_token_secret = 'Z**B*************U***yZ**B*************U***y'

# authorization of consumer key and consumer secret key
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# set access to user's access key and access secret key
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()

'''
#print(user.followers_count)
#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#   print(tweet.text)
'''

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)

#To retweet tweets with specified strings
search_string = 'EXO-SC'
numberOfTweets = 5

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
    try:
        tweet.retweet()
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break




'''
#  Generous Bot : Follows back 
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
   if follower.name == 'abcdef':
       follower.follow()
       break
'''