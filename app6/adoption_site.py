import os 
from flask import Flask , render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 
from forms import AddForm, DelForm


app = Flask(__name__) 

app.config['SECRET_KEY'] = 'mysecretkey'

#############################
########## SQL SETUP ########
#############################

base_dir = os.path.abspath(os.path.dirname(__file__)) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(base_dir, 'database.sqlite') 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) 
Migrate(app, db)

#############################
########### MODELS ##########
#############################

class Puppy(db.Model) : 
    __tablename__ = 'puppies' 
    id = db.Column(db.Integer, primary_key = True) 
    name  = db.Column(db.Text) 

    def __init__(self, name): 
        self.name = name 

    def __repr__(self): 
        return f"Puppy Name: {self.name}"


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add', methods = ['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        new_puppy = Puppy(name)
        db.session.add(new_puppy) 
        db.session.commit()
        return redirect(url_for('list_pup'))
    return render_template('add.html', form = form)

@app.route('/list_pup')
def list_pup():
    puppies = Puppy.query.all()
    return render_template('list.html', puppies = puppies)

@app.route('/del_pup')
def del_pup():
    form = DelForm() 
    if(form.validate_on_submit) :
        id = form.id.data 
        puppy = Puppy.query.get(id) 
        db.session.delete(puppy) 
        db.session.commit()
        return redirect(url_for('list_pup'))
    return render_template('delete.html', form = form)


if __name__ == "__main__":
    app.run(debug=True)



