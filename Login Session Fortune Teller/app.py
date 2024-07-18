from flask import Flask, render_template, request, redirect, url_for, session
from datetime import timedelta
import secrets
import random  # Ensure random is imported

app = Flask(__name__,
            template_folder='templates',
            static_folder='static')

app.secret_key = secrets.token_hex(16)
app.permanent_session_lifetime = timedelta(minutes=5)

fortunes = [
    "Don't be panicked because of CS.",
    "Life is nice.",
    "Don't let CS ruin your life.",
    "If you have an error:",
    "1. Breathe.",
    "2. Smile.",
    "3. Ask for help from your mates.",
    "4. Ask for help from your TA or Instructor.",
    "5. And you're done!",
    "Have a nice day BTW."
]

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.permanent = True
        user = request.form['name']
        birth_month = request.form['birth_month']
        session['user'] = user
        session['birth_month'] = birth_month
        return redirect(url_for('home'))
    if 'user' in session:
        return redirect(url_for('home'))
    return render_template('login_page.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        birth_month = request.form['birth_month']
        return redirect(url_for('fortune', birth_month=birth_month))
    
    return render_template('hello.html')  # Updated template name

@app.route('/fortune/<birth_month>')
def fortune(birth_month):
    index = len(birth_month) % len(fortunes)
    chosen_fortune = fortunes[index]
    fortune_text = f"Your fortune is: {chosen_fortune}"
    return render_template('fortune.html', fortune=fortune_text, birth_month=birth_month)

@app.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('birth_month', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
