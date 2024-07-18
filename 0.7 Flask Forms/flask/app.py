from flask import Flask, render_template,url_for,redirect,request
import random

app = Flask(__name__,
template_folder='templates',
static_folder='static')
fortunes=[
    "Dont be panick bbecause of CS", #Supposed to be comma in list
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
    if request.method == 'POST':
        birth_month = request.form['birth_month']
        
        #checking for user input 
        if birth_month:
            index = len(birth_month)
            chosen_fortune = fortunes[index]
            fortune_text = f"Your fortune is: {chosen_fortune}"
        else:
            # This for if birth_month is not provided, it will choose a random fortune from the list
            chosen_fortune = random.choice(fortunes)
            fortune_text = f"Your random fortune is: {chosen_fortune}"
   
        if index > 10:  
            return render_template('fortune.html', fortune = "Error", birth_month=birth_month)  
        else: 
            return render_template('fortune.html', fortune=fortune_text, birth_month=birth_month)
    else:
        return render_template('hello.html')

    

    
  
    # number_of_birth_month = len(birth_month)
    # number_of_the_list = len(fortunes)
    # if number_of_birth_month > number_of_the_list:
    #     return render_template('fortune.html', fortune = "error")  
    # else: 
    #     return render_template('fortune.html', fortune=fortune_text)  

if __name__ == '__main__':
    app.run(debug=True)