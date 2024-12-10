from flask import Flask, render_template, request
from transformers import OpenAIApi

app = Flask(__name__)
openai = OpenAIApi(api_key="YOUR_OPENAI_API_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
  if request.method == "POST":
    name = request.form["name"]
    experience = request.form["experience"]
    skills = request.form["skills"]
    education = request.form["education"]

    prompt = f"""
    Write a professional resume for {name} with the following information:

    Experience: {experience}
    Skills: {skills}
    Education: {education}
    """

    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      max_tokens=500,
      temperature=0.7,
    )
    resume = response.choices[0].text

    return render_template("index.html", resume=resume)
  else:
    return render_template("index.html")

if __name__ == "__main__":
  app.run(debug=True)