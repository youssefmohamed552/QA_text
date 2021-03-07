import torch.nn as nn
import torch

device = torch.device('cude' if torch.cuda.is_available() else 'cpu')

class QuestionEncoder(nn.Module):
  def __init__(self, input_dim, hidden_dim, max_length=10):
    super(QuestionEncoder, self).__init__()
    self.hidden_dim = hidden_dim
    self.gru = nn.GRU(input_dim, hidden_dim)

  def forward(self, x):
    hidden = self.initHidden()
    for word in x:
      word = word.view(1, 1, -1)
      output, hidden = self.gru(word.float(), hidden)
    return hidden

  def initHidden(self):
    return torch.zeros(1, 1, self.hidden_dim, device=device)


    

