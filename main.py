from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            .error {{ color: red; }}
        </style>
    </head>
    <body>
        <h1>Signup</h1>
        <form method="post">
            <table>
                <tbody>
                    <tr>
                        <td>
                            <label for="username">Username</label>
                        </td>
                        <td>
                            <input name="username" type="text" value='{username}' />
                            <span class="error">{username_error}</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label for="password">Password</label>
                        </td>
                        <td>
                            <input name="password" type="password" value='{password}' />
                            <span class="error">{password_error}</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label for="verify">Verify Password</label>
                        </td>
                        <td>
                            <input name="verify" type="password" value='{verify}' />
                            <span class="error">{verify_error}</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label for="email">Email (optional)</label>
                        </td>
                        <td>
                            <input name="email" value='{email}' />
                            <span class="error">{email_error}</span>
                        </td>
                    </tr>
                </tbody>
            </table>
            <input type="submit">
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

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
        username_error = "That's not a valid username"
        username = ''
    else:
        if ' ' in username:
            username_error = "That's not a valid username"        
            username = ''
        else:
            if len(username) < 3 or len(username) > 20:
                username_error = "That's not a valid username"        
                username = ''

    if password == '':
        password_error = "That's not a valid password"
        password = ''
    else:
        if ' ' in password:
            password_error = "That's not a valid password"        
            password = ''
        else:
            if len(password) < 3 or len(password) > 20:
                password_error = "That's not a valid password"        
                password = ''

    if verify != password:
        verify_error = "Passwords don't match"
        verify = ''
    
    if ' ' in email:
        email_error = "That's not a valid email"        
        email = ''
    else:
        if '@' not in email:
            email_error = "That's not a valid email"        
            email = ''
        else:
            if '.' not in email:
                email_error = "That's not a valid email"
                email = ''
    
    if not username_error and not password_error and not verify_error and not email_error:
        return '<h1>Welcome, ' + username + '!</h1>'
    else:
        return form.format(username=username, username_error=username_error, 
            password=password, password_error=password_error, 
            verify=verify, verify_error=verify_error, 
            email=email, email_error=email_error)

app.run()