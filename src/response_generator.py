import torch.nn as nn
import torch

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

class ResponseGenerator(nn.Module):
  def __init__(self, word_encoder, input_dim, hidden_dim):
    super(ResponseGenerator, self).__init__()
    self.word_encoder = word_encoder
    self.hidden_dim = hidden_dim
    self.linear = nn.Linear(input_dim, hidden_dim)
    self.gru = nn.GRU(hidden_dim, hidden_dim)

  def forward(self, x1, x2):
    hidden = self.initHidden()
    x = torch.cat((x1, x2), dim=2)
    y = self.linear(x)
    # statement = []
    # start_symbol = self.word_encoder.decode_word('startext')
    # output, hidden = self.gru(start_symbol, y)
    # for i in range(10):
      # word = word.view(1, 1, -1)
      # output, hidden = self.gru(output, hidden)
    return hidden

  def initHidden(self):
    return torch.zeros(1, 1, self.hidden_dim, device=device)
