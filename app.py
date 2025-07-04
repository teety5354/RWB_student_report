from flask import Flask, request, render_template, redirect, url_for, session, flash, g
import sqlite3
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import bcrypt

app = Flask(__name__)
DATABASE = 'student.db'
app.secret_key = 'your-secret-key'  # Required for session login

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('rwb-sb-account-db-55ee40ed4a2d.json', scope)
client = gspread.authorize(creds)
sheet = client.open('RWB-SR Account Database').sheet1 # Google Sheets

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(error):
    db = g.pop('db', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    student_id = request.args.get('studentID', '').strip()
    db = get_db()
    cur = db.execute('SELECT * FROM students WHERE id = ?', (student_id,))
    row = cur.fetchone()
    if row:
        return render_template('result.html', student=row, student_id=student_id)
    else:
        return render_template('result.html')

# @app.route('/login')
# def login():
#     return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username_input = request.form['username']
        password_input = request.form['password']

        users = sheet.get_all_records()
        user = next((u for u in users if u['username'] == username_input), None)

        if user:
            stored_hash = user['password_hash']
            if bcrypt.checkpw(password_input.encode('utf-8'), stored_hash.encode('utf-8')):
                session['user'] = username_input
                return redirect(url_for('dashboard'))
            else:
                flash("Incorrect Username or Password", "error")
        else:
            flash("404 User Not Found", "error")

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return f"Welcome, {session['user']}!"

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request

app = Flask(__name__)

# ตัวอย่างฐานข้อมูลจำลอง
students = {
}

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/search')
def search():
    student_id = request.args.get('studentID').strip()
    student = students.get(student_id)
    return render_template('result.html', student=student, student_id=student_id)

@app.route('/login')
def login():
    return render_template('login.html')