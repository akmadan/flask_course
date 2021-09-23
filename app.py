from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    answer = {'akshit': 'madan'}
    namesList = ['Akshit', 'Aasif', 'Gaurav']
    return render_template('index.html', name= 'Akshit', 
    answer = answer, passedList = namesList, user_logged_in=True) #String name and dict answer are passed to html file

if __name__ == '__main__':
    app.run(debug=True)
 

