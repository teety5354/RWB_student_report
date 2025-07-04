# RWB Student Report

## สิ่งที่ต้องใช้:
[**Python**](https://www.python.org/downloads/) (3.9 ขึ้นไป)

[**venv & Flask**](https://flask.palletsprojects.com/en/stable/installation/#python-version)

## เดี๋ยวจะได้ใช้:
[**JavaScript**](https://www.java.com/en/)

[**docker**](https://www.docker.com/get-started/)  (ใช้ลง node.js/npm)

[**npm & node.js**](https://nodejs.org/en/download) (backend สำหรับ login & password hashing/encryption)

[**Google API & Service**](https://console.cloud.google.com/) (ใช้เชื่อม google sheets เป็น database)

(สามารถกดลิงค์เพื่ออ่านคู่มือ/วิธีการลง Library พวกนี้ได้เลย)

## วิธีการ Run ในเครื่อง
รันโค้ดด้วย CMD 

แก้โค้ดด้วย ***VScode/Python***

เข้าถึงโฟลเดอร์ที่มีไฟล์อยู่ เช่น
**cd "C:\Users\user\Documents\RWB student report"** (ตาม Path ในเครื่องตัวเอง)

รัน venv ก่อนรัน app.py (.venv\Scripts\activiate)

ให้ขึ้น (venv) C:\Users\user\Documents\RWB student report> แสดงว่าถูกต้อง

python (ชื่อไฟล์).(นามสกุลไฟล์) เช่น >python app.py

## ถ้าไม่มีโฟลเดอร์venv

python -m venv venv

venv\Scripts\activate

pip install flask gspread oauth2client bcrypt
# for prime\
cd ที่อยู่
venv\Scripts\activate
py app.py
