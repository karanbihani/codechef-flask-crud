from flask import Flask, render_template, request, redirect, url_for, flash

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

# def create_app():
#     app = Flask(__name__)

#     with app.app_context():
#         init_db()

#     return app

app = Flask(__name__)
app.secret_key = "Secret Key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:bihani123@localhost/crud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.app_context().push()

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
    all_data = data.query.all()
    #return "Welcome to Crud application."

    return render_template("index.html", employees = all_data)

@app.route('/newemp/')
def newEmp():
    return render_template("newemp.html")

@app.route('/editemp/<id>/')
def editEmp(id):
    my_data = data.query.get(id)
    return render_template("editemp.html", my_data = my_data)

@app.route('/insert/', methods=['POST'])
def insert():

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

    my_data = data(name,email,phone)
    db.session.add(my_data)
    db.session.commit()

    return redirect(url_for("index"))


@app.route('/update', methods=['GET','POST'])
def update():
    if request.method == 'POST':
        my_data = data.query.get(request.form.get('id'))
    
    my_data.name = request.form['name']
    my_data.email = request.form['email']
    my_data.phone = request.form['phone']

    db.session.commit()
    
    return redirect(url_for("index"))

@app.route('/delete/<id>/', methods = ["GET", "POST"])
def delete(id):
    my_data = data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()

    #data.query.filter_by(id=123).delete()
    return redirect(url_for("index"))
    

if __name__ == "__main__":
    app.run(debug = True)