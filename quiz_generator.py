
import random

# df- pandas dataframe storing all the data  
# quiz_questions- dictionary to store unique questions in the quiz
def generate_question(df, quiz_questions, quiz_answers):
  length = len(df)-1
  qnum = random.randint(0,length)

  while qnum in quiz_questions:
    qnum = random.randint(0,length)

  country = df.iloc[qnum, 1]
  capital = df.iloc[qnum, 2]

  answers_set = set()
  answers_set.add(capital)

  while len(answers_set) < 4:
    anum = random.randint(0,length)
    cap = df.iloc[anum, 2]
    if cap not in answers_set:
      answers_set.add(cap)

  quiz_questions[country] = list(answers_set)
  quiz_answers[country] = capital

def generate_question7(df, quiz_questions, quiz_answers):
  length = len(df)-1
  qnum = random.randint(0,length)

  while qnum in quiz_questions:
    qnum = random.randint(0,length)
  
  country = df.iloc[qnum, 1]
  export = df.iloc[qnum, 12]

  answers_set = set()
  answers_set.add(export)

  while len(answers_set) < 4:
    anum = random.randint(0,length)
    cap = df.iloc[anum, 12]
    if cap not in answers_set:
      answers_set.add(cap)

  quiz_questions[country] = list(answers_set)
  quiz_answers[country] = export

def generate_question2(df, quiz_questions, quiz_answers):
  length = len(df)-1
  qnum = random.randint(0,length)

  while qnum in quiz_questions:
    qnum = random.randint(0,length)

  country = df.iloc[qnum, 1]
  famous_place = df.iloc[qnum, 10]

  answers_set = set()
  answers_set.add(famous_place)

  while len(answers_set) < 4:
    anum = random.randint(0,length)
    cap = df.iloc[anum, 10]
    if cap not in answers_set:
      answers_set.add(cap)

  quiz_questions[country] = list(answers_set)
  quiz_answers[country] = famous_place

def generate_question3(df, quiz_questions, quiz_answers):
  length = len(df)-1
  qnum = random.randint(0,length)
    
  while qnum in quiz_questions:
    qnum = random.randint(0,length)
  
  country = df.iloc[qnum, 1]
  continent = df.iloc[qnum, 3]
  
  answers_set = set()
  answers_set.add(continent)
    
  while len(answers_set) < 4:
    anum = random.randint(0,length)
    cap = df.iloc[anum, 3]
    if cap not in answers_set:
      answers_set.add(cap)

  quiz_questions[country] = list(answers_set)
  quiz_answers[country] = continent

def generate_question4(df, quiz_questions, quiz_answers):
  length = len(df)-1
  qnum = random.randint(0,length)

  while qnum in quiz_questions:
    qnum = random.randint(0,length)
 
  country = df.iloc[qnum, 1]
  population = df.iloc[qnum, 4]
 
  answers_set = set()
  answers_set.add(population)
   
  while len(answers_set) < 4:
    anum = random.randint(0,length)
    cap = df.iloc[anum, 4]
    if cap not in answers_set:
      answers_set.add(cap)

  quiz_questions[country] = list(answers_set)
  quiz_answers[country] = population

def generate_question5(df, quiz_questions, quiz_answers):
  length = len(df)-1
  qnum = random.randint(0,length)

  while qnum in quiz_questions:
    qnum = random.randint(0,length)
 
  country = df.iloc[qnum, 1]
  language = df.iloc[qnum, 7]
 
  answers_set = set()
  answers_set.add(language)
   
  while len(answers_set) < 4:
    anum = random.randint(0,length)
    cap = df.iloc[anum, 7]
    if cap not in answers_set:
      answers_set.add(cap)

  quiz_questions[country] = list(answers_set)
  quiz_answers[country] = language

def generate_question6(df, quiz_questions, quiz_answers):
  length = len(df)-1
  qnum = random.randint(0,length)

  while qnum in quiz_questions:
    qnum = random.randint(0,length)
 
  country = df.iloc[qnum, 1]
  currency = df.iloc[qnum, 9]
 
  answers_set = set()   
  answers_set.add(currency)
   
  while len(answers_set) < 4:
    anum = random.randint(0,length)
    cap = df.iloc[anum, 9]
    if cap not in answers_set:
      answers_set.add(cap)

  quiz_questions[country] = list(answers_set)
  quiz_answers[country] = currency

def get_country_capitals(df):
  length = len(df)-1
  country_capitals = {}  
  for i in range(length):
    qnum = i
    country = df.iloc[qnum, 1]
    capital = df.iloc[qnum, 2]
    country_capitals[i] = country + " : " + capital
  return country_capitals

def get_continent(df):
  length = len(df)-1
  country_continent = {}
  for i in range(length):
    qnum = i
    country = df.iloc[qnum, 1]
    continent = df.iloc[qnum, 3]
    country_continent[i] = country + " : " + continent
  return country_continent

def get_population(df):
  length = len(df)-1
  country_population = {}
  for i in range(length):
    qnum = i
    country = df.iloc[qnum, 1]
    population = df.iloc[qnum, 4]
    country_population[i] = country + " : " + population
  return country_population

def get_language(df):
  length = len(df)-1
  country_language = {}
  for i in range(length):
    qnum = i
    country = df.iloc[qnum, 1]
    language = df.iloc[qnum, 7]
    country_language[i] = country + " : " + language
  return country_language

def get_currency(df):
  length = len(df)-1
  country_currency = {}
  for i in range(length):
    qnum = i
    country = df.iloc[qnum, 1]
    currency = df.iloc[qnum, 9]
    country_currency[i] = country + " : " + currency
  return country_currency

def get_site(df):
  length = len(df)-1
  country_sites = {}
  for i in range(length):
    qnum = i
    country = df.iloc[qnum, 1]
    famous_place = df.iloc[qnum, 10]
    link = df.iloc[qnum, 11]
    country_sites[i] = country + " : " + famous_place + " : " + link
  return country_sites

def get_export(df):
  length = len(df)-1
  country_export = {}
  for i in range(length):
    qnum = i
    country = df.iloc[qnum, 1]
    export = df.iloc[qnum, 12]
    country_export[i] = country + " : " + export
  return country_export


