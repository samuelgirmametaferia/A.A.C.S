import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/prompt')
def get_prompt():
  response = openai.Completion.create(
    engine="text-davinci-003",
    prompt="Generate a creative writing prompt.",
    max_tokens=50,
    temperature=0.7
  )
  return jsonify({'prompt': response.choices[0].text.strip()})

if __name__ == '__main__':
  app.run(debug=True)

"logic_puzzle_game.cs"