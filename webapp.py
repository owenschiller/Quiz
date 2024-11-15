import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.  
# For more info see: https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY

app.secret_key=os.environ["SECRET_KEY"]; #This is an environment variable.  
                                     #The value should be set on the server. 
                                     #To run locally, set in env.bat (env.sh on Macs) and include that file in gitignore so the secret key is not made public.

@app.route('/')
def renderMain():
    return render_template('home.html')

@app.route('/startOver')
def startOver():
    session.clear() #clears variable values and creates a new session
    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

@app.route('/page1')
def renderPage1():
    return render_template('page1.html')

@app.route('/page2',methods=['GET','POST'])
def renderPage2():
    # with open("questions.json") as data:
        # questions = json.load(data)
    
   
        
    session["year"]=request.form['year']
    
    # session["lastName"]=request.form['lastName']
    return render_template('page2.html')
    # answers = questions[1]["Answers"]

@app.route('/page3',methods=['GET','POST'])
def renderPage3():
    # session["favoriteColor"]=request.form['favoriteColor']
    return render_template('page3.html')

@app.route('/page4',methods=['GET','POST'])
def renderPage4():
    # session["favoriteColor"]=request.form['favoriteColor']
    return render_template('page4.html', count = amount())
def amount():
    
    count = 0
    if session['year'] == "2009":
        count+=1
        
   
    return count
if __name__=="__main__":
    app.run(debug=False)
