from flask import Flask, render_template
import random
app = Flask(__name__,
template_folder='templates',
static_folder='static')

@app.route('/home')
def home():
    return render_template('hello.html')

@app.route('/fortune')
def fortune():
    fortune=[
    "Dont be panick bbecause of CS"
    "Life is nice"
    "Dont let CS ruin your life"
    "If you have an error:"
    "1.Breath"
    "2.Smile"
    "3.Ask for help from your mates"
    "4.Ask for help from your TA or Instructor"
    "5.And your done!!!!"
    "Have a nice day BTW"
    ]

    choserandomly= random.choice(fortune)
    return render_template('fortune.html', fortune=choserandomly)

if __name__ == '__main__':
    app.run(debug = True)