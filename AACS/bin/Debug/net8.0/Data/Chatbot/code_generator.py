import openai

openai.api_key = "YOUR_API_KEY"

def generate_code(prompt):
  response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=100,
    temperature=0.7
  )
  return response.choices[0].text.strip()

while True:
  user_input = input("Enter code snippet request: ")
  generated_code = generate_code(user_input)
  print("Generated Code:\n", generated_code)