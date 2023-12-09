from flask import Flask, render_template, request, flash
import sqlite3
import os
from dotenv import load_dotenv


app = Flask(__name__)
load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


def dbConnection():
    connection = sqlite3.connect('Cyberebels.db')
    connection.row_factory = sqlite3.Row

    return connection

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contacts', methods=('GET', 'POST'))
def contact_form():
    if request.method == 'POST':
        email = request.form['email']
        fname = request.form['fname']
        lname = request.form['lname']
        inquiry = request.form['inquiry']
        phone = request.form['phone']

        db = dbConnection()
        db.execute('INSERT INTO Inquiries (email, description, first_name, last_name, phone) VALUES (?,?,?,?,?)', 
                   (email, inquiry, fname, lname, phone))
        #  cur.execute('INSERT INTO Posts (title, description, first_name, last_name) VALUES (?,?,?,?)', 
                    # (title, desc, firstName, lastName))

        db.commit()
        db.close()

        flash('Thank you for submitting your inquiry, we will get back to your shortly.')
    
        
    return render_template('contact.html')



