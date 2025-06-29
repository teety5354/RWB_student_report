import sqlite3

conn = sqlite3.connect('student.db')
cur = conn.cursor()

# ลบนักเรียนที่มี ID = '37871'
cur.execute("DELETE FROM students WHERE id = ?", ('37575',))

conn.commit()
conn.close()

print("🗑️ ลบข้อมูลเรียบร้อยแล้ว")