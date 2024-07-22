from flask import Flask, render_template, request, redirect, session, url_for
import pyrebase

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

Config = {
    "apiKey": "AIzaSyDSlzpcauMpjdvXBRo3IOWu4Yi6S_GwqNU",
    "authDomain": "auth-lab-bfd14.firebaseapp.com",
    "projectId": "auth-lab-bfd14",
    "storageBucket": "auth-lab-bfd14.appspot.com",
    "messagingSenderId": "53978111196",
    "appId": "1:53978111196:web:33254ef92b816de25f6819",
    "measurementId": "G-76KPB174YX",
    "databaseURL": ""
}

firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()

@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.create_user_with_email_and_password(email, password)
            session['user'] = user['idToken']
            session['quotes'] = []
            return redirect(url_for('home'))
        except Exception as e:
            return f"Error creating account: {e}"
    return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] = user['idToken']
            session['quotes'] = []
            return redirect(url_for('home'))
        except Exception as e:
            return f"Error signing in: {e}"
    return render_template('signin.html')

@app.route('/signout', methods=['POST'])
def signout():
    auth.current_user = None
    session.clear()
    return redirect(url_for('signin'))

@app.route('/home', methods=['GET', 'POST'])
def home():
    if 'user' not in session:
        return redirect(url_for('signin'))
    if request.method == 'POST':
        quote = request.form['quote']
        session['quotes'].append(quote)
        session.modified = True

        return redirect(url_for('thanks'))
    return render_template('home.html')

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

@app.route('/display')
def display():
    if 'user' not in session:
        return redirect(url_for('signin'))
    return render_template('display.html', quotes=session['quotes'])

if __name__ == '__main__':
    app.run(debug=True)

