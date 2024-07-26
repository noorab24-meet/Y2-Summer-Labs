from flask import Flask, render_template, request, redirect, session, url_for
import pyrebase

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

Config= {
  "apiKey": "AIzaSyDSlzpcauMpjdvXBRo3IOWu4Yi6S_GwqNU",
  "authDomain": "auth-lab-bfd14.firebaseapp.com",
  "databaseURL": "https://auth-lab-bfd14-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "auth-lab-bfd14",
  "storageBucket": "auth-lab-bfd14.appspot.com",
  "messagingSenderId": "53978111196",
  "appId": "1:53978111196:web:33254ef92b816de25f6819",
  "measurementId": "G-76KPB174YX",
}


firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()
db =firebase.database()

@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        full_name = request.form['full_name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.create_user_with_email_and_password(email, password)
            session['user'] = user['idToken']
            session['user_id'] = user['localId']
            session['user_name'] = full_name
            user_data = {
                "full_name": full_name,
                "email": email,
                "username": username
            }
            db.child("Users").child(user['localId']).set(user_data)
            session['quotes'] = []
            return redirect(url_for('home'))
        except Exception as e:
            error_message = str(e)
            return render_template('error.html', error_message=error_message)
    return render_template('signup.html')


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] = user['idToken']
            session['user_id'] = user['localId']
            session['quotes'] = []
            return redirect(url_for('home'))
        except Exception as e:
            error_message = str(e)
            return render_template('error.html', error_message=error_message)
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
        quote_text = request.form['quote']
        session.modified = True
        said_by = request.form['speaker']
        additional_info = request.form.get('additional_info', '')
        quote_dict = {
            "quote": quote_text,
            "speaker": said_by,
            "additional_info": additional_info,
            "uid": session['user']
        }
        db.child("Quotes").push(quote_dict)
        return redirect(url_for('thanks'))
    return render_template('home.html')    


@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

@app.route('/display')
def display():
    if 'user' not in session:
        return redirect(url_for('signin'))
    quotes = db.child("Quotes").get().val()
    if quotes is None:
        quotes = []
    else:
        quotes = list(quotes.values())
    return render_template('display.html', quotes=quotes)


if __name__ == '__main__':
    app.run(debug=True)

