# this is just a test file
from __future__ import print_function

import grpc

import ProseAndBabel_pb2
import ProseAndBabel_pb2_grpc

def run():
 channel = grpc.insecure_channel('localhost:50050')
 stub = ProseAndBabel_pb2_grpc.ProseAndBabelStub(channel)
 response = stub.GetHaiku(ProseAndBabel_pb2.BabelRequest())
 print("A Haiku 4 U:")
 print(response.response)
 response = stub.GetBabel(ProseAndBabel_pb2.BabelRequest())
 print("Markovian Babel:")
 print(response.response)

if __name__ == '__main__':
  run()
