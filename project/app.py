from flask import Flask, render_template, request, redirect, session, url_for
import pyrebase

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'
Config = {
    "apiKey": "AIzaSyCgz8BSxm5S89AGm4ll2Zf9VC6zvW1l-Fw",
    "authDomain": "mini-b8c41.firebaseapp.com",
    "databaseURL": "https://mini-b8c41-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "mini-b8c41",
    "storageBucket": "mini-b8c41.appspot.com",
    "messagingSenderId": "1024786217286",
    "appId": "1:1024786217286:web:369d0f6121782450278d47",
    "measurementId": "G-T82QJE1X40"
}

firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()
db = firebase.database()

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

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
            return redirect(url_for('account'))
        except Exception as e:
            error_message = str(e)
            return render_template('error.html', error_message=error_message)
    return render_template('signin.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.create_user_with_email_and_password(email, password)
            session['user'] = user['idToken']
            session['user_id'] = user['localId']
            session['user_name'] = full_name
            session['user_email'] = email
            user_data = {
                "full_name": full_name,
                "email": email,
                "movies": []
            }
            db.child("Users").child(user['localId']).set(user_data)
            session['quotes'] = []
            return redirect(url_for('account'))
        except Exception as e:
            error_message = str(e)
            return render_template('error.html', error_message=error_message)
    return render_template('signup.html')

@app.route('/account')
def account():
    if 'user' in session:
        user_id = session['user_id']
        user_data = db.child("Users").child(user_id).get().val()
        movies = user_data.get("movies", [])
        return render_template('account.html', user=user_data, movies=movies)
    return redirect(url_for('signin'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('user_id', None)
    session.pop('user_name', None)
    session.pop('user_email', None)
    return redirect(url_for('home'))

@app.route('/addToMyList', methods=['POST'])
def addToMyList():
    if 'user' in session:
        user_id = session['user_id']
        movie_title = request.form.get('movie')  
        user_data = db.child("Users").child(user_id).get().val()
        movies = user_data.get("movies", [])
        if movie_title and movie_title not in movies:
            movies.append(movie_title)
            db.child("Users").child(user_id).update({"movies": movies})
        return redirect(url_for('account'))
    return redirect(url_for('signin'))



@app.route('/showasguest', methods=['GET', 'POST'])
def showasguest():
    return render_template('moviestype.html')

@app.route('/moviestype', methods=['GET', 'POST'])
def moviestype():
    return render_template('moviestype.html')

@app.route('/action', methods=['GET'])
def action():
    return render_template('action.html')

@app.route('/comedy', methods=['GET'])
def comedy():
    return render_template('comedy.html')

@app.route('/crime', methods=['GET'])
def crime():
    return render_template('crime.html')

@app.route('/lift_movie', methods=['GET', 'POST'])
def lift_movie():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        review = request.form['review']
        review_data = {
            "user_id": session.get('user_id', 'guest'),
            "name": name,
            "email": email,
            "review": review
        }
        db.child("Reviews").child('lift_movie').push(review_data)
        return redirect(url_for('lift_movie'))
    
    reviews = db.child("Reviews").child('lift_movie').get().val() or {}
    return render_template('lift_movie.html', reviews=reviews)

@app.route('/looper_movie', methods=['GET', 'POST'])
def looper_movie():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        review = request.form['review']
        review_data = {
            "user_id": session.get('user_id', 'guest'),
            "name": name,
            "email": email,
            "review": review
        }
        db.child("Reviews").child('looper_movie').push(review_data)
        return redirect(url_for('looper_movie'))
    
    reviews = db.child("Reviews").child('looper_movie').get().val() or {}
    return render_template('looper_movie.html', reviews=reviews)

@app.route('/island_movie', methods=['GET', 'POST'])
def island_movie():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        review = request.form['review']
        review_data = {
            "user_id": session.get('user_id', 'guest'),
            "name": name,
            "email": email,
            "review": review
        }
        db.child("Reviews").child('island_movie').push(review_data)
        return redirect(url_for('island_movie'))
    
    reviews = db.child("Reviews").child('island_movie').get().val() or {}
    return render_template('island_movie.html', reviews=reviews)

@app.route('/players_movie', methods=['GET', 'POST'])
def players_movie():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        review = request.form['review']
        review_data = {
            "user_id": session.get('user_id', 'guest'),
            "name": name,
            "email": email,
            "review": review
        }
        db.child("Reviews").child('players_movie').push(review_data)
        return redirect(url_for('players_movie'))
    
    reviews = db.child("Reviews").child('players_movie').get().val() or {}
    return render_template('players_movie.html', reviews=reviews)

@app.route('/redone_movie', methods=['GET', 'POST'])
def redone_movie():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        review = request.form['review']
        review_data = {
            "user_id": session.get('user_id', 'guest'),
            "name": name,
            "email": email,
            "review": review
        }
        db.child("Reviews").child('redone_movie').push(review_data)
        return redirect(url_for('redone_movie'))
    
    reviews = db.child("Reviews").child('redone_movie').get().val() or {}
    return render_template('redone_movie.html', reviews=reviews)


@app.route('/irishwish_movie', methods=['GET', 'POST'])
def irishwish_movie():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        review = request.form['review']
        review_data = {
            "user_id": session.get('user_id', 'guest'),
            "name": name,
            "email": email,
            "review": review
        }
        db.child("Reviews").child('irishwish_movie').push(review_data)
        return redirect(url_for('irishwish_movie'))
    
    reviews = db.child("Reviews").child('irishwish_movie').get().val() or {}
    return render_template('irishwish_movie.html', reviews=reviews)
    
@app.route('/damaged_movie', methods=['GET', 'POST'])
def damaged_movie():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        review = request.form['review']
        review_data = {
            "user_id": session.get('user_id', 'guest'),
            "name": name,
            "email": email,
            "review": review
        }
        db.child("Reviews").child('damaged_movie').push(review_data)
        return redirect(url_for('damaged_movie'))
    
    reviews = db.child("Reviews").child('damaged_movie').get().val() or {}
    return render_template('damaged_movie.html', reviews=reviews)

@app.route('/knivesout_movie', methods=['GET', 'POST'])
def knivesout_movie():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        review = request.form['review']
        review_data = {
            "user_id": session.get('user_id', 'guest'),
            "name": name,
            "email": email,
            "review": review
        }
        db.child("Reviews").child('knivesout_movie').push(review_data)
        return redirect(url_for('knivesout_movie'))
    
    reviews = db.child("Reviews").child('knivesout_movie').get().val() or {}
    return render_template('knivesout_movie.html', reviews=reviews)         


@app.route('/boneyard_movie', methods=['GET', 'POST'])
def boneyard_movie():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        review = request.form['review']
        review_data = {
            "user_id": session.get('user_id', 'guest'),
            "name": name,
            "email": email,
            "review": review
        }
        db.child("Reviews").child('boneyard_movie').push(review_data)
        return redirect(url_for('boneyard_movie'))
    
    reviews = db.child("Reviews").child('boneyard_movie').get().val() or {}
    return render_template('boneyard_movie.html', reviews=reviews) 


if __name__ == '__main__':
    app.run(debug=True)
