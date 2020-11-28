import requests as r
import GetOldTweets3 as got
import markovify as m

def handler(event, context):
    criteria = got.manager.TweetCriteria().setUsername("realDonaldTrump").setMaxTweets(5)
    tweets = got.manager.TweetManager.getTweets(criteria)
    print(tweets)