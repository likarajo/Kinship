import os
import sys
from lib.operations import kinships

print('****Welcome to the Kinship tool****')
i_word = input('Enter the WORD: ')
i_kins = input('Enter the required no. of KINS: ')
i_tweet_count = input('Enter the required no. of TWEETS to fetched: ')

kinships(
    ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN'],
    ACCESS_SECRET = os.environ['TWITTER_ACCESS_TOKEN_SECRET'],
    CONSUMER_KEY = os.environ['TWITTER_CONSUMER_KEY'],
    CONSUMER_SECRET = os.environ['TWITTER_CONSUMER_SECRET'],
    word = i_word,
    kins = int(i_kins),
    tweet_count = int(i_tweet_count)
)
