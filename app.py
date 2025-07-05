from flask import Flask, request, render_template, redirect, url_for, session, flash, g
import sqlite3
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import bcrypt

app = Flask(__name__)
DATABASE = 'student.db'
app.secret_key = 'your-secret-key'  # session login

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('rwb-sb-account-db-da8565c59ec7.json', scope)
client = gspread.authorize(creds)
accountdata = client.open('RWB-SR Account Database').sheet1 # connecting account data google sheets naja
studentdata = client.open('RWB-SR Student Database').sheet1

DEDUCTION_REASONS = {
    "101-123": ("", 5),
    "201-211": ("", 10),
    "301-309": ("", 20),
    "401-412": ("", 30),
    "501-509": ("ประเภท ปค.2", 30),
    "510-512": ("ประเภท ปค.2 (สิ่งเสพติด)", 30),
    "อื่นๆ": ("", 0),  # ต้องกรอกรายละเอียดเพิ่มเติม
}

# def get_db():
#     if 'db' not in g:
#         g.db = sqlite3.connect(DATABASE)
#         g.db.row_factory = sqlite3.Row
#     return g.db

# @app.teardown_appcontext
# def close_db(error):
#     db = g.pop('db', None)
#     if db is not None:
#         db.close()

@app.route('/')
def index():
    if 'user' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

# @app.route('/search')
# def search():
#     student_id = request.args.get('studentID', '').strip()
#     db = get_db()
#     cur = db.execute('SELECT * FROM students WHERE id = ?', (student_id,))
#     row = cur.fetchone()
#     if row:
#         return render_template('result.html', student=row, student_id=student_id)
#     else:
#         return render_template('result.html')

# @app.route('/search')
# def search():
#     student_id = request.args.get('studentID', '').strip()
#     students = studentdata.get_all_records()
#     student = next((s for s in students if str(s['id']) == student_id), None)

#     return render_template('result.html', student=student, student_id=student_id, deduction_reasons=DEDUCTION_REASONS)


@app.route('/search', methods=['GET', 'POST'])
def search():
    student_id = request.values.get('studentID', '').strip()
    students = studentdata.get_all_records()

    student = None
    row_index = None
    for idx, s in enumerate(students, start=2):
        if str(s['id']) == student_id:
            student = s
            row_index = idx
            break

    if request.method == 'POST':
        if 'user' not in session:
            flash("ต้องเข้าสู่ระบบก่อน", "error")
            return redirect(url_for('login'))

        reason_code = request.form['reason_code']
        reason_text, deduct_score = DEDUCTION_REASONS.get(reason_code, ("ไม่ทราบเหตุผล", 0))

        if reason_code == "513":
            custom_detail = request.form.get("custom_reason_detail", "").strip()
            if custom_detail:
                reason_text = f"513 - {custom_detail}"

        try:
            current_score = int(student['behaviour score'])
            new_score = max(0, current_score - deduct_score)
            # Update score
            studentdata.update_cell(
                row_index,
                list(student.keys()).index('behaviour score') + 1,
                new_score
            )

            # Optional: log this deduction to a separate sheet
            logsheet = client.open("RWB-SR Deduction Log").sheet1
            logsheet.append_row([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                student['id'],
                student['surname'] + ' ' + student['lastname'],
                reason_text,
                deduct_score,
                session['user']
            ])

            # Refresh student
            students = studentdata.get_all_records()
            student = next((s for s in students if str(s['id']) == student_id), None)

            flash(f"หักคะแนนสำเร็จ: {deduct_score} คะแนน ({reason_text})", "success")
        except Exception as e:
            flash("เกิดข้อผิดพลาด: ไม่สามารถหักคะแนนได้", "error")

    return render_template(
        'result.html',
        student=student,
        student_id=student_id,
        deduction_reasons=DEDUCTION_REASONS
    )

# @app.route('/login')
# def login():
#     return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user' in session:
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        username_input = request.form['username']
        password_input = request.form['password']

        users = accountdata.get_all_records()
        user = next((u for u in users if u['username'] == username_input), None)

        if user:
            stored_hash = user['password_hash']
            if bcrypt.checkpw(password_input.encode('utf-8'), stored_hash.encode('utf-8')):
                session['user'] = username_input
                return redirect(url_for('dashboard'))
            else:
                flash("Incorrect Username or Password", "error")
        else:
            flash("Incorrect Username or Password", "error")

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', user=session['user'])

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)