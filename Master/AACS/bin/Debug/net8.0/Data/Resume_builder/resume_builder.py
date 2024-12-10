from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    name = request.form['name']
    experience = request.form['experience']
    skills = request.form['skills']
    return render_template('resume.html', name=name, experience=experience, skills=skills)
  return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)