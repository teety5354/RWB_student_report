# RWB Student Report

## สิ่งที่ต้องใช้:
[**Python**](https://www.python.org/downloads/) (3.9 ขึ้นไป)

[**venv & Flask**](https://flask.palletsprojects.com/en/stable/installation/#python-version)

[**JavaScript**](https://www.java.com/en/)

[**Google API & Service**](https://console.cloud.google.com/) (ใช้เชื่อม google sheets เป็น database)

**gspread oauth2client bcrypt**

(สามารถกดลิงค์เพื่ออ่านคู่มือ/วิธีการลง Library พวกนี้ได้เลย)
## โปรเจคนี้ต้องใช้ไฟล์ account-service.json:
ไฟล์นี้ใช้สำหรับเชื่อมข้อมูลระหว่าง backend กับ database และไม่สามารถ commit ลง GitHub ได้ ไม่งั้นจะถูกผิดทิ้งทันที

ถ้าหากต้องการไฟล์ account-service.json ให้ขอมาทาง Discord DM ***เท่านั้น***

เมื่อได้ไฟล์ไปแล้วให้วางไว้ในที่เดียวกันกับ app.py

### ห้ามเปลี่ยนชื่อหรือโค้ดข้างในไฟล์ account-service.json หรือ .gitignore เด็ดขาด
### ห้าม commit account-service.json เป็นอันเด็ดขาด!!!!!!!!!

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
