import random

questions = [
    {"question": "What is the capital of France?", "options": ["Berlin", "Paris", "Madrid", "Rome"], "answer": "Paris"},
    {"question": "What is the highest mountain in the world?", "options": ["K2", "Kangchenjunga", "Mount Everest", "Lhotse"], "answer": "Mount Everest"},
    {"question": "Who painted the Mona Lisa?", "options": ["Michelangelo", "Raphael", "Leonardo da Vinci", "Donatello"], "answer": "Leonardo da Vinci"}
]

score = 0

def ask_question(question):
  print(question["question"])
  for i, option in enumerate(question["options"]):
    print(f"{i+1}. {option}")

  while True:
    try:
      answer = int(input("Enter your answer (1-4): "))
      if 1 <= answer <= 4:
        break
      else:
        print("Invalid input. Please enter a number between 1 and 4.")
    except ValueError:
      print("Invalid input. Please enter a number.")

  return question["options"][answer-1] == question["answer"]

for question in questions:
  if ask_question(question):
    score += 1

print(f"You got {score} out of {len(questions)} questions correct.")