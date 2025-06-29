import sqlite3

# เชื่อมต่อกับไฟล์ student.db (ถ้ายังไม่มีจะสร้างให้)
conn = sqlite3.connect('student.db')
cur = conn.cursor()

# สร้างตารางนักเรียน
cur.execute('''
CREATE TABLE IF NOT EXISTS students (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    grade TEXT
)
''')

# เพิ่มข้อมูลตัวอย่าง
students = [
    ('S001', 'Alice', 'A'),
    ('S002', 'Bob', 'B'),
    ('S003', 'Charlie', 'C')
]
cur.executemany('INSERT OR IGNORE INTO students VALUES (?, ?, ?)', students)

# บันทึกและปิดการเชื่อมต่อ
conn.commit()
conn.close()

print("✅ สร้างตารางและเพิ่มข้อมูลเรียบร้อยแล้ว")