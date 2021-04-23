import os
from dotenv import load_dotenv
from sqlalchemy import MetaData
from flask import Flask, jsonify, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from http import HTTPStatus
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
import sqlite3 as sql
from datetime import datetime
from flask_mail import Mail, Message
from event import Event_handler

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///complaints.db'
db = SQLAlchemy(app)

load_dotenv()

# Email messenger
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587 
app.config['MAIL_USERNAME'] = os.getenv('EMAIL')
app.config['MAIL_PASSWORD'] = os.getenv('PASSWORD')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)


class complain(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    store_name = db.Column(db.String(200))
    date_added = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return '<Task %r>' % self.id

db.create_all()               

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
    

@app.route('/service',methods = ['POST', 'GET'])
def service():
    return render_template('service.html')

@app.route('/complaint',methods = ['POST', 'GET'])
def complaint():
    return render_template('complaint.html')    


@app.route('/delete')
def delete():
    return render_template('delete.html')

@app.route('/update')
def update():
    return render_template('update.html')




@app.route('/addcomplaint', methods = ['POST', 'GET'])
def addcomplaint():
    name = request.form.get('name')
    description = request.form.get('description')
    store_name = request.form.get('store_name')
    date_added = datetime.utcnow().isoformat()
            
    # create new user with the form data. Hash the password so plaintext version isn't saved.
    new_store = complain(name=name,description=description,store_name=store_name, date_added=date_added)

    # add the new user to the database and send notification
    db.session.add(new_store)
    db.session.commit()
    
    Event_handler()
    message = "added successfully"
    return render_template("message_added.html",message = message)




@app.route('/deletecomplaint', methods = ['POST', 'GET'])
def deletecomplaint():
    if request.method == 'POST':
        try:

            id = request.form['id']

            new_store = complain.query.filter_by(id=id).one()
            db.session.delete(new_store)
            db.session.commit()
            message = "Complain deleted successfully!"

        except:
            message = "Error in deleting complain"

        finally:

            return render_template("msg_update_delete.html", message=message)

# list entire table
@app.route('/list')
def list():
    list = complain.query.all()
   
    return render_template("list.html",list=list)   

@app.route('/updatecomplaint', methods = ['POST', 'GET'])
def updatecomplaint():
    if request.method == 'POST':
        try:
            
            id = request.form['id']
            name = request.form.get('name')
            description = request.form.get('description')
            store_name = request.form.get('store_name')

            #x = Store.query.filter_by(id=id).one()
            x=complain(id=id,name=name,description=description,store_name=store_name)

            db.session.merge(x)
            db.session.commit()
          
            message = "Complain updated successfully!"

        except:
            message = "Error in updating complain"

        finally:

            return render_template("msg_update_delete.html", message=message)
    

if  __name__ =="__main__":
    app.run(debug=True)    