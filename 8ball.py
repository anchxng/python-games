# Import modules
import sys
import random

answer_list = [
  "It is certain",
  "Outlook good",
  "You may rely on it",
  "Ask again later",
  "Concentrate and ask again",
  "Better not tell you now",
  "Don't count on it",
  "My sources say no",
  "Very doubtful",
]

while True:
  question = input("Ask the magic 8 ball a question: (press enter to quit): ")
  answers = random.randrange(9)

  if question == "":
    sys.exit()

  print(answer_list[answers])

