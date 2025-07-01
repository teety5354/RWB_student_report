import sqlite3

conn = sqlite3.connect('student.db')
cur = conn.cursor()

# ลบนักเรียนที่มี ID = '37871'
#('37617', 'ปัณณวิชญ์ จรูญภาค', '100'))
cur.execute("DELETE FROM students WHERE id = ?", ('37575',))
cur.execute("DELETE FROM students WHERE id = ?", ('37871',))
cur.execute("DELETE FROM students WHERE id = ?", ('37577',))
cur.execute("DELETE FROM students WHERE id = ?", ('37586',))
cur.execute("DELETE FROM students WHERE id = ?", ('37615',))
cur.execute("DELETE FROM students WHERE id = ?", ('37617',))
conn.commit()
conn.close()

print("🗑️ ลบข้อมูลเรียบร้อยแล้ว")