from flask import Flask, request, render_template, g
import sqlite3

app = Flask(__name__)
DATABASE = 'student.db'

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

@app.route('/login')
def login():
    return render_template('login.html')

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