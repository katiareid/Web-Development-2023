from flask import Flask, render_template
import sqlite3
from sqlite3 import Error

app = Flask(__name__)
DATABASE = "music_mental.db"

def create_connection(db_file):
  try:
    connection = sqlite3.connect(db_file)
    return connection
  except Error as e:
    print(e)
  return None

@app.route('/')
def render_base():
    return render_template('home.html')

@app.route('/about')
def render_about():
    return render_template('about.html')

@app.route('/age-service-hours')
def render_ageservicehours():
    return render_template('ageservicehours.html')

@app.route('/workinstrumentgenre')
def render_workinstrumentgenre():
    return render_template('workinstrumentgenre.html')

@app.route('/anixetydepressioninsomnia')
def render_anxietydepressioninsomnia():
    return render_template('anixetydepressioninsomnia.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)
  