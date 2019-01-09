import tweepy
import requests
from credentials import *
import twitter
import pytz
from datetime import datetime

#
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth)

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret)

# Need to change me to current time zone before release to production!!!!!!!!!!!!!!!!!!
last_run = datetime.strptime("Tue Jan 07 21:38:51 +0000 2019", "%a %b %d %H:%M:%S %z %Y")

def parse_time(time_string):
    time = datetime.strptime(time_string, "%a %b %d %H:%M:%S %z %Y")
    return time

def needs_response(mention):
    return parse_time(mention) > last_run

def new_mentions():
    mentions = api.GetSearch(raw_query="q=%40botquixotic&src=typd")

    mentions_list = []
    for mention in mentions:
        user_mention = []
        if needs_response(mention.created_at):
            user_mention.append(mention.user.screen_name)
            user_mention.append(mention.id)
            mentions_list.append(user_mention)

    last_run = datetime.utcnow().replace(tzinfo=pytz.utc)
    return mentions_list

def get_timeline(screen_name):
    all_updates = api.GetUserTimeline(screen_name=screen_name, count=200)
    text = []
    for status in all_updates:
        text.append(status.text)

    text = "".join(text)
    return text


def new_friends():
    results = api.GetFollowers()
    return "stuff"

def post_mention(screen_name, prose, id):
    prose = "@" + screen_name + " " + prose + screen_name
    api.PostUpdate(prose, in_reply_to_status_id=id)
