import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

app.secret_key=os.environ["secret_key"]; 

@app.route('/')
def renderMain():
    return render_template('home.html')

@app.route('/startOver')
def startOver():
    session.clear() #clears variable values and creates a new session
    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

@app.route('/page1')
def renderPage1():
    with open("questions.json") as data:
        questions = json.load(data)
        
    # session["lastName"]=request.form['lastName']
    return render_template('page1.html', answers = questions[0]["Answers"])


@app.route('/page2',methods=['GET','POST'])
def renderPage2():
    with open("questions.json") as data:
        questions = json.load(data)
        
    session["year"]=request.form['year']
    # session["lastName"]=request.form['lastName']
    return render_template('page2.html', answers = questions[1]["Answers"])

@app.route('/page3',methods=['GET','POST'])
def renderPage3():
    # session["favoriteColor"]=request.form['favoriteColor']
    return render_template('page3.html')
    
@app.route('/page4',methods=['GET','POST'])
def renderPage4():
    # session["favoriteColor"]=request.form['favoriteColor']
    return render_template('page4.html')
def amount():
    count = ""
    

if __name__=="__main__":
    app.run(debug=True)
