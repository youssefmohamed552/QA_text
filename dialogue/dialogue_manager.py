class DialogueManager:
  def __init__(self):
    print('starting the dialogue manager')
    # self.question = input('how can I help you?')
    self.question = 'who is romeo'
    # self.response = input()

  def step(self):
    print('step')
    self.get_question()
    self.get_response()

  def get_question(self):
    self.question = input()

  def get_response(self):
    self.response = input()
