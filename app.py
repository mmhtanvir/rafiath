from flask import Flask, url_for, render_template, redirect, request, session
import datetime 
from flask_mysqldb import MySQL
import mysql.connector

app = Flask(__name__, static_url_path='/static')
app.config['UPLOAD_FOLDER'] = 'static/images'


app.secret_key = 'your-secret-key'


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'rafiath'  
# get data with db column name instead of index
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

@app.route("/")
def index():
        if 'email' in session:
            email = session['email']
        else:
            email = None 
        return render_template('index.html', email = email)

@app.route("/feelona-admin")
def admin():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM admin")
    data = cur.fetchall()
    cur.close()

    if 'user_id' in session:
        username = session['user_id']
        user_id = username  # Assigning the value of 'user_id'
    else:
        user_id = None  

    if 'user_id' not in session:
        # User is not logged in, redirect them to the login page
        return redirect(url_for('login'))

    return render_template("admin.html", userId=user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        sql = "SELECT id, email, password from users WHERE email = %s"
        cur = mysql.connection.cursor()
        cur.execute(sql, (email,))
        user = cur.fetchone()
        cur.close()

        if user and password == user['password']:
            session['email'] = user['email']

            return redirect(url_for('index'))
        else:
            return render_template('login.html', error="Invalid email or Password")

    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        cur = mysql.connection.cursor()

        sql = "INSERT INTO users (name, email, password) VALUES(%s, %s, %s)"
        data = (name, email, password)
        cur.execute(sql, data)
        cur.close()
        mysql.connection.commit()
        return redirect(url_for('login'))

    return render_template('sign_up.html')

@app.route('/fflog', methods=['GET', 'POST'])
def flogin():

    if request.method == 'POST':
        user_id = request.form['user_id']
        password = request.form['password']

        sql = "SELECT id, user_id, password FROM admin WHERE user_id = %s"
        cur = mysql.connection.cursor()
        cur.execute(sql, (user_id,))
        user = cur.fetchone()
        cur.close()

        if user and password == user['password']:
            session['user_id'] = user['user_id']
            return redirect(url_for('admin'))
        else:
            return render_template('admin_login.html', error="Invalid id or Password")

    return render_template('admin_login.html')

@app.route('/ffid', methods=['GET', 'POST'])
def fsignup():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        user_id = request.form['user_id']
        password = request.form['password']
        
        cur = mysql.connection.cursor()

        # Check if the id already exists in the database
        cur.execute("SELECT * FROM admin WHERE user_id = %s", (user_id,))
        existing_user = cur.fetchone()

        if existing_user:
            cur.close()
            return render_template('admin_sign_up.html', error = "User ID already exists. Please choose a different user id.")
        else:
            # Insert new user data into the database
            sql = "INSERT INTO admin (name, email, password, user_id) VALUES(%s, %s, %s, %s)"
            data = (name, email, password, user_id)
            cur.execute(sql, data)
            cur.close()
            mysql.connection.commit()
            return redirect(url_for('flogin'))

    return render_template('admin_sign_up.html')

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)