import sqlite3

conn = sqlite3.connect('student.db')
cur = conn.cursor()

# 1. สร้างตารางใหม่
cur.execute('''
CREATE TABLE students_new (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    score TEXT
)
''')

# 2. คัดลอกข้อมูลจากตารางเก่า
cur.execute('INSERT INTO students_new (id, name, score) SELECT id, name, grade FROM students')

# 3. ลบตารางเก่า
cur.execute('DROP TABLE students')

# 4. เปลี่ยนชื่อตารางใหม่
cur.execute('ALTER TABLE students_new RENAME TO students')

conn.commit()
conn.close()

print("✅ เปลี่ยนชื่อคอลัมน์จาก grade → score เรียบร้อยแล้ว")