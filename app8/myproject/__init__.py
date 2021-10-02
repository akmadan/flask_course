import os 
from flask import Flask 
from flask_login import LoginManager 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 

login_manager = LoginManager()


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

login_manager.init_app(app) 
login_manager.login_view = 'login'

#############################
########### MODELS ##########
#############################
