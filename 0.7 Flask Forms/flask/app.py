from flask import Flask, render_template,url_for,redirect,request
import random

app = Flask(__name__,
template_folder='templates',
static_folder='static')
fortunes=[
    "Dont be panick bbecause of CS", #Supposed to be comma in list!!
    "Life is nice",
    "Dont let CS ruin your life",
    "If you have an error:",
    "1.Breath",
    "2.Smile",
    "3.Ask for help from your mates",
    "4.Ask for help from your TA or Instructor",
    "5.And your done!!!!"
    "Have a nice day BTW"
       ]

@app.route('/home', methods=['GET', 'POST'])
def home():
    # if request.method == 'POST':
    #     birth_month = request.form['birth_month']
    #     return redirect(url_for('fortune', birth_month=birth_month))
    # else:
    #     return render_template('hello.html')

     # Check if birth_month is passed as a query parameter
    if request.method == 'GET':
        return render_template('hello.html')
    else:
        birth_month = request.form['birth_month']

        #default text
        fortune_text = "no fortune default"

        if birth_month:
            index = len(birth_month)
            chosen_fortune = fortunes[index]
            fortune_text = f"Your fortune is: {chosen_fortune}"
        else:
            # This for if birth_month is not provided, it will choose a random fortune from the list
            chosen_fortune = random.choice(fortunes)
            fortune_text = f"Your random fortune is: {chosen_fortune}"

        return render_template('fortune.html', fortune=fortune_text)   


# @app.route('/fortune')
# def fortune():
#     # Check if birth_month is passed as a query parameter
#     birth_month = request.form['birth_month']

#     #default text
#     fortune_text = "no fortune default"

#     if birth_month:
#         index = len(birth_month)
#         chosen_fortune = fortunes[index]
#         fortune_text = f"Your fortune is: {chosen_fortune}"
#     else:
#         # This for if birth_month is not provided, it will choose a random fortune from the list
#         chosen_fortune = random.choice(fortunes)
#         fortune_text = f"Your random fortune is: {chosen_fortune}"

#     return render_template('fortune.html', fortune=fortune_text)


# def fortune():
#     birth_month = request.args.get('birth_month')
#     if birth_month:
#         random.seed(birth_month)  #  I uesed it for seed random with birth_month
#         chosen_fortune = random.choice(fortunes)
#         fortune_text = "Your fortune for " + birth_month + " is: " + chosen_fortune
#     else:
#         chosen_fortune = random.choice(fortunes) #  I puted for choosing a random fortune
#         fortune_text = "Your random fortune is: " + chosen_fortune

#     return render_template('fortune.html', fortune=fortune_text)


if __name__ == '__main__':
    app.run(debug=True)