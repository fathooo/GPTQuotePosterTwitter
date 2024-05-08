
import tweepy
from app.config import ENVIRONMENTS

api_key = ENVIRONMENTS['twitter_api_key']
api_secret = ENVIRONMENTS['twitter_api_secret']
bearer_token = ENVIRONMENTS['twitter_bearer_token']
access_token = ENVIRONMENTS['twitter_access_token']
access_token_secret = ENVIRONMENTS['twitter_access_token_secret']

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)


def create_tweet(text):
    try:
        client.create_tweet(text = text)
    except Exception as e:
        print(e)