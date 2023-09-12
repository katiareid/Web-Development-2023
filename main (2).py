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

@app.route('/categories1')
def render_ageservicehours():
  query = "SELECT ID, Age, Primary_streaming_service, Hours_per_day FROM music"
  con = create_connection(DATABASE)
  cur = con.cursor()

  cur.execute(query)
  tag_list = cur.fetchall()
  con.close()
  print(tag_list)
  return render_template('categories1.html', tags=tag_list)

@app.route('/sort/<title>')
def render_sortpage(title):
    sort = request.args.get('sort')
    order = request.args.get('order', 'asc')  # Get the current sort order, default to 'asc' if not provided

    # Toggle the sort order
    if order == 'asc':
        new_order = 'desc'
    else:
        new_order = 'asc'

    # Sort query
    query = "SELECT ID, Age, Primary_streaming_service, Hours_per_day FROM music ORDER BY " + sort + " " + order
    
    con = create_connection(DATABASE)
    cur = con.cursor()
    
    # Query the DATABASE
    cur.execute(query, (title,))
    tag_list = cur.fetchall()
    con.close()

    return render_template('categories1.html', tags=tag_list, title=title, types=get_types(), order=new_order)

@app.route('/categories2')
def render_workinstrumentgenre():
   query = "SELECT ID, While_working, Instrumentalist, Fav_genre FROM music"
   con = create_connection(DATABASE)
   cur = con.cursor()

   cur.execute(query)
   tag_list = cur.fetchall()
   con.close()
   print(tag_list)
   return render_template('categories2.html', tags=tag_list)

@app.route('/categories3')
def render_anxietydepressioninsomnia():
   query = "SELECT ID, Anxiety, Depression, Insomnia FROM music"
   con = create_connection(DATABASE)
   cur = con.cursor()

   cur.execute(query)
   tag_list = cur.fetchall()
   con.close()
   print(tag_list)
   return render_template('categories3.html', tags=tag_list)
  

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)
  