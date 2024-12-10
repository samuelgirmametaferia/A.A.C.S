import random

def generate_question(topic):
  questions = {
    "history": ["Who was the first president of the United States?", "What year did World War II begin?"],
    "science": ["What is the chemical formula for water?", "What is the largest planet in our solar system?"],
    "math": ["What is the square root of 16?", "What is the formula for calculating the area of a circle?"]
  }
  return random.choice(questions[topic])

def check_answer(user_answer, correct_answer):
  if user_answer.lower() == correct_answer.lower():
    return "Correct!"
  else:
    return "Incorrect. The correct answer is: " + correct_answer

while True:
  topic = input("What topic would you like to study? (history, science, math): ")
  question = generate_question(topic)
  print(question)
  user_answer = input("Your answer: ")
  result = check_answer(user_answer, question)
  print(result)