import sqlite3

conn = sqlite3.connect('student.db')
cur = conn.cursor()

# เพิ่มข้อมูลนักเรียนใหม่
cur.execute("INSERT OR IGNORE INTO students (id, name, score) VALUES (?, ?, ?)", 
            ('37617', 'ปัณณวิชญ์ จรูญภาค', '100'))

conn.commit()
conn.close()

print("✅ เพิ่มนักเรียนเรียบร้อยแล้ว")


#รันด้วย cmd 