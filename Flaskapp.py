from sqlalchemy import MetaData
from flask import Flask, jsonify, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from http import HTTPStatus
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
import sqlite3 as sql
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./Barky/bookmarks.db'
db = SQLAlchemy(app)

class bookmarks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(200), nullable=False)
    notes = db.Column(db.String(200))
    date_added = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return '<Task %r>' % self.id

#db.create_all()               

@app.route('/', methods=['POST','GET'])
def index():
    return render_template('index.html')

@app.route('/addbookmark', methods = ['POST', 'GET'])
def addbookmark():
   
    return render_template("AddBookmark.html")
   

'''@app.route('/newbookmark', methods = ['POST', 'GET'])
def newbookmark():
   
    return "<h> Bookmark added </h><a href = '/'>Go back to options page</a>" ''' 


@app.route('/adddata', methods = ['POST', 'GET'])
def adddata():
    if request.method == 'POST':
        try:
            
            engine = create_engine('sqlite:///./Barky/bookmarks.db', echo = True)
            meta = MetaData()

            bookmarks = Table('bookmarks', meta, 
            Column('id', Integer, primary_key = True), 
            Column('title', String), 
            Column('url', String), 
            Column('notes', String), 
            Column('date_added', String), 
            )

            conn = engine.connect()
           
            id = request.form['id']
            title = request.form['title']
            url = request.form['url']
            notes = request.form['notes']
            date_add = datetime.utcnow().isoformat()
            
            data = bookmarks.insert().values(id = id, title = title, url = url, notes = notes, date_added = date_add)
            result = conn.execute(data)

            message = "Bookmark added successfully"

        except:
            message = "There was an issue with inserting data"

        finally:
            return render_template("message.html",message = message)


@app.route('/table')
def table():
    bookmark = bookmarks.query.all()

   
    return render_template("table.html",bookmark=bookmark)       

if  __name__ =="__main__":
    app.run(debug=True)    