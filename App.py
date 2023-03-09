from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

app = Flask(__name__)
app.secret_key = "Secret Key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:"bihani123"@localhost/crud_codechef'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class data(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

@app.route('/')
def index():
    return render_template("index.html")
    #return "Welcome to Crud application."

@app.route('/newemp/')
def newEmp():
    return render_template("newemp.html")

@app.route('/editemp/')
def editEmp():
    return render_template("editemp.html")

if __name__ == "__main__":
    app.run(debug = True)