from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

#user-signup

@app.route("/user-info", methods=['POST'])

def user_form():
    username=request.form['username']
    password=request.form['password']
    verifypassword=request.form['verifypassword']
    email=request.form['email']

    name_error = ""
    pw_error = ""
    verify_error = ""
    email_error = "" 

    if username == '':
        name_error="That's not a valid username"

    elif username == ' ':
        name_error="Username must not contain any spaces"

    elif len(username) < 3 or len(username) > 20:
        name_error="Username must meet the length requirement"
        

    if password == '':
        pw_error="That's not a valid password"

    elif password == ' ':
        pw_error="Password must not contain any spaces"

    elif len(password) < 3 or len(password) > 20:
        pw_error="Password must meet the length requirement"


    if verifypassword != password:
        verify_error="Passwords don't match"

    elif verifypassword == '':
        verify_error="That's not a valid password"


    if email != '':
        if '@' not in email and '.' not in email:
            email_error="Please enter a valid email address"

        if '@' not in email or '.' not in email:
            email_error="Please enter a valid email address"

        if ' ' in email:
                email_error="Email must not contain any spaces"

    if not name_error and not pw_error and not verify_error and not email_error:
        return render_template('welcome.html', username=username)

    else:
        return render_template('index.html', username=username, name_error=name_error, pw_error=pw_error, verify_error=verify_error, email_error=email_error, email=email)

@app.route("/")
def index():

    return render_template('index.html')
    
app.run()
