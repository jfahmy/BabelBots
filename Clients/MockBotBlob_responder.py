from __future__ import print_function
import grpc

import MockBotBlob_twitterapi

import ProseAndBabel_pb2
import ProseAndBabel_pb2_grpc

from time import sleep


def run():
 channel = grpc.insecure_channel('localhost:50050')
 stub = ProseAndBabel_pb2_grpc.ProseAndBabelStub(channel)

 # tweets ? at folks that interact
 users = MockBotBlob_twitterapi.new_mentions()
 for user in users:
     full_text = MockBotBlob_twitterapi.get_timeline(user[0])
     response = stub.UserMarkov(ProseAndBabel_pb2.UserTweets(tweets=full_text))
     MockBotBlob_twitterapi.post_mention(user[0], response.prose, user[1])

 # checks for new follows and follows back
 MockBotBlob_twitterapi.new_friends()

if __name__ == '__main__':
  run()
