from flask import Flask, render_template
import pandas as pd
import json
from flask import jsonify
import quiz_generator

app = Flask(__name__)
df = pd.read_csv('data.csv')
print(df)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/information')
def information():
    return render_template('information.html')

@app.route('/capital')
def capital():
  country_capitals = quiz_generator.get_country_capitals(df)
  return render_template('capital.html', country_capitals=json.dumps(country_capitals))

@app.route('/export')
def export():
  country_export = quiz_generator.get_export(df)
  return render_template('export.html', country_export=json.dumps(country_export))

@app.route('/continent')
def continent():
  country_continent = quiz_generator.get_continent(df)
  return render_template('continent.html', country_continent=json.dumps(country_continent))
  
@app.route('/qcontinent')
def qcontinent():
  print("Starting quiz3")
  quiz_questions, quiz_answers = start_quiz3()
  print("Generating quiz3");
  return render_template('qcontinent.html', title="page", json_questions=json.dumps(quiz_questions), json_answers=json.dumps(quiz_answers))

@app.route('/population')
def population():
  country_population = quiz_generator.get_population(df)
  return render_template('popul.html', country_population=json.dumps(country_population))

@app.route('/qpopulation')
def qpopulation():
  quiz_questions, quiz_answers = start_quiz4()
  return render_template('qpopul.html', title="page", json_questions=json.dumps(quiz_questions), json_answers=json.dumps(quiz_answers))

@app.route('/economy')
def economy():
    return render_template('economy.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/qeconomy')
def qeconomy():
    return render_template('qeconomy.html')

@app.route('/qcapital')
def qcapital():
    quiz_questions, quiz_answers = start_quiz()
    return render_template('qcapital.html', title="page", json_questions=json.dumps(quiz_questions), json_answers=json.dumps(quiz_answers))

def start_quiz():
  quiz_questions = {}
  quiz_answers = {}

  while len(quiz_questions) < 10:
    quiz_generator.generate_question(df, quiz_questions, quiz_answers)
  return quiz_questions, quiz_answers

def start_quiz2():
  quiz_questions = {}
  quiz_answers = {}

  while len(quiz_questions) < 10:
    quiz_generator.generate_question2(df, quiz_questions, quiz_answers)
  return quiz_questions, quiz_answers

def start_quiz3():
  quiz_questions = {}
  quiz_answers = {}

  while len(quiz_questions) < 10:
    quiz_generator.generate_question3(df, quiz_questions, quiz_answers)
  return quiz_questions, quiz_answers

def start_quiz4():
  quiz_questions = {}
  quiz_answers = {}

  while len(quiz_questions) < 10:
    quiz_generator.generate_question4(df, quiz_questions, quiz_answers)
  return quiz_questions, quiz_answers

def start_quiz5():
  quiz_questions = {}
  quiz_answers = {}

  while len(quiz_questions) < 10:
    quiz_generator.generate_question5(df, quiz_questions, quiz_answers)
  return quiz_questions, quiz_answers


def start_quiz6():
  quiz_questions = {}
  quiz_answers = {}

  while len(quiz_questions) < 10:
    quiz_generator.generate_question6(df, quiz_questions, quiz_answers)
  return quiz_questions, quiz_answers

@app.route('/state')
def state():
    return render_template('state.html')

@app.route('/famous_places')
def famous_places():
  country_sites = quiz_generator.get_site(df)
  return render_template('fp.html', country_sites=json.dumps(country_sites))

@app.route('/qfamous_places')
def qfamous_places():
  quiz_questions, quiz_answers = start_quiz2()
  return render_template('qfp.html', title="page", json_questions=json.dumps(quiz_questions), json_answers=json.dumps(quiz_answers))

@app.route('/government')
def government():
    return render_template('gover.html')

@app.route('/qgovernment')
def qgovernment():
    return render_template('qgover.html')

@app.route('/currency')
def currency():
  country_currency = quiz_generator.get_currency(df)
  return render_template('currency.html', country_currency=json.dumps(country_currency))

@app.route('/qcurrency')
def qcurrency():
  quiz_questions, quiz_answers = start_quiz6()
  return render_template('qcurren.html', title="page", json_questions=json.dumps(quiz_questions), json_answers=json.dumps(quiz_answers))

@app.route('/language')
def language():  
  country_language = quiz_generator.get_language(df)
  return render_template('lang.html', country_language=json.dumps(country_language))

@app.route('/qlanguage')
def qlanguage():
  quiz_questions, quiz_answers = start_quiz5()
  return render_template('qlang.html', title="page", json_questions=json.dumps(quiz_questions), json_answers=json.dumps(quiz_answers))

#Run the app:
if __name__ == "__main__":
    app.run()
