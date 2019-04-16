from flask import Flask, request, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template("sign_up.html")

@app.route("/", methods=['POST'])
def sign_up():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if username == '':
        username_error = "Username can't be left blank"
        username = ''
    else:
        if ' ' in username:
            username_error = "Username can't contain spaces"        
            username = ''
        else:
            if len(username) < 3 or len(username) > 20:
                username_error = "Username must be between 3 and 20 characters long"        
                username = ''

    if password == '':
        password_error = "Password can't be left blank"
        password = ''
    else:
        if ' ' in password:
            password_error = "Password can't contain spaces"        
            password = ''
        else:
            if len(password) < 3 or len(password) > 20:
                password_error = "Password must be between 3 and 20 characters long"        
                password = ''

    if verify == '':
        verify_error = "Verify can't be left blank"
        verify = ''
    else:
        if ' ' in verify:
            verify_error = "Verify can't contain spaces"        
            verify = ''
        else:
            if len(verify) < 3 or len(verify) > 20:
                verify_error = "Verify must be between 3 and 20 characters long"        
                verify = ''    
            else:
                if verify != password:
                    verify_error = "Verify doesn't match password"
                    verify = ''
    
    if email != '':
        if ' ' in email:
            email_error = "Email can't contain spaces"        
            email = ''
        else:
            if len(email) < 3 or len(email) > 20:
                email_error = "Email must be between 3 and 20 characters long"        
                email = ''
            else:
                if email.count('@') != 1 and email.count('.') != 1:
                    email_error = "Email must contain one @ and one .(dot)"        
                    email = ''

            
    if not username_error and not password_error and not verify_error and not email_error:
        return render_template("welcome.html", username = username)
    else:
        return render_template("sign_up.html", username=username, username_error=username_error, 
            password=password, password_error=password_error, 
            verify=verify, verify_error=verify_error, 
            email=email, email_error=email_error)

app.run()