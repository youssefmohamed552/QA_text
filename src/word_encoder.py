import torch
import numpy as np

class WordEncoder:
  def __init__(self):
    self.word_map = {}
    self.word_map_rev = {}
    with open('glove.6B.100d.txt') as f:
      print('START parsing word encodings ... ')
      for line in f.readlines():
        l = line.strip().split(' ')
        word = l[0]
        tensor = torch.tensor(np.array([float(x) for x in l[1:]]))
        self.word_map[word] = tensor
        self.word_map[tensor] = word
      print('DONE parsing word encodings ... ')
      print('num of words parsed: ', len(self.word_map))

  def encode_word(self, word):
    return self.word_map[word]



  def encode_statement(self, statement):
    encoded_statement = []
    for word in statement.strip().split(' '):
      encoded_statement.append(self.word_map[word])

    return encoded_statement
      

  def decode_word(self, encoded_word):
    return self.word_map_rev[encoded_word]

  def decoded_statement(self, encoded_statement):
    statement = []
    for eword in encoded_statement:
      statement.append(self.word_map_rev[eword])

    return statement
