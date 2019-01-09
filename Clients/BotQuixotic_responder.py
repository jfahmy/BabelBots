from __future__ import print_function
import grpc

import BotQuixotic_twitterapi

import ProseAndBabel_pb2
import ProseAndBabel_pb2_grpc

from time import sleep


def run():
 channel = grpc.insecure_channel('localhost:50050')
 stub = ProseAndBabel_pb2_grpc.ProseAndBabelStub(channel)

 # tweets haikus at anyone who has tweeted at bot
 users = BotQuixotic_twitterapi.new_mentions()
 for user in users:
     full_text = BotQuixotic_twitterapi.get_timeline(user[0])
     response = stub.UserHaiku(ProseAndBabel_pb2.UserTweets(tweets=full_text))
     BotQuixotic_twitterapi.post_mention(user[0], response.prose, user[1])

 # checks for new follows and follows back
 BotQuixotic_twitterapi.new_friends()

if __name__ == '__main__':
  run()
