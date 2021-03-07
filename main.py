from dialogue.dialogue_manager import DialogueManager
from src.qa_text import QA_text
from src.word_encoder import WordEncoder

def main():
  print('welcome to the qa_text program')
  text = '''
  this is who wrote the main story of romeo and juliet
  '''
  dialogue = DialogueManager()
  word_encoder = WordEncoder()
  # word_encoder = None
  qa_text = QA_text(word_encoder)
  qa_text(dialogue.question, text)
  # dialogue.step()

if __name__ == '__main__':
  main()
