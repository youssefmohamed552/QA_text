import torch.nn as nn
import torch

from src.question_understanding import QuestionEncoder
from src.text_understanding import TextEncoder
from src.response_generator import ResponseGenerator
# from src.word_encoder import WordEncoder

class QA_text(nn.Module):
  def __init__(self, word_encoder):
    super(QA_text, self).__init__()
    self.word_encoder = word_encoder
    self.question_encoder = QuestionEncoder(input_dim=100, hidden_dim=100)
    self.text_encoder = TextEncoder(input_dim=100, hidden_dim=100)
    self.response_generator = ResponseGenerator(word_encoder=word_encoder, input_dim=200, hidden_dim = 100)


  def forward(self, question, text):
    encoded_question = self.word_encoder.encode_statement(question)
    encoded_text = self.word_encoder.encode_statement(text)
    encoded_question = [torch.rand(100) for _ in range(5)]
    encoded_text = [torch.rand(100) for _ in range(100)]
    out_question = self.question_encoder(encoded_question)
    out_text = self.text_encoder(encoded_text)
    out_response = self.response_generator(out_question, out_text)
    print('out_question : ', out_question)
    print('out_text : ', out_text)
    print('out_response : ', out_response)


