from __future__ import print_function
import grpc

import twitterapi

import ProseAndBabel_pb2
import ProseAndBabel_pb2_grpc

from time import sleep


def run():
 channel = grpc.insecure_channel('localhost:50050')
 stub = ProseAndBabel_pb2_grpc.ProseAndBabelStub(channel)

 # tweets ? at folks that interact
 users = twitterapi.new_mentions()
 for user in users:
     full_text = twitterapi.get_timeline(user[0])
     # response = stub.UserHaiku(ProseAndBabel_pb2.UserTweets(tweets=full_text))
     twitterapi.post_mention(user[0], response.prose, user[1])

 # checks for new follows and follows back
 twitterapi.new_friends()

if __name__ == '__main__':
  run()
