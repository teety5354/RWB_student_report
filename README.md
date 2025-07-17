# สิ่งที่ต้องใช้:
- [**Python**](https://www.python.org/downloads/) (3.9 ขึ้นไป)
- [**venv & Flask**](https://flask.palletsprojects.com/en/stable/installation/#python-version)
- [**JavaScript**](https://www.java.com/en/)
- [**Google API & Service**](https://console.cloud.google.com/) (ใช้เชื่อม google sheets เป็น database) ***ต้องใช้ไฟล์ account-service.json ซึ่งอธิบายอยู่ด้านล่าง***
- **gspread oauth2client bcrypt**
- [**datetime**](https://docs.python.org/3/library/datetime.html) (สำหรับทำ log/ประวัติการลบคะแนน) (เดี๋ยวจะได้ใช้)
## โปรเจคนี้ต้องใช้ไฟล์ account-service.json:
ไฟล์นี้ใช้สำหรับเชื่อมข้อมูลระหว่าง backend กับ database และไม่สามารถ commit ลง GitHub ได้ ไม่งั้นจะถูกผิดทิ้งทันที

ถ้าหากต้องการไฟล์ account-service.json ให้ขอมาทาง Discord DM ***เท่านั้น***

เมื่อได้ไฟล์ไปแล้วให้วางไว้ในที่เดียวกันกับ app.py

### ห้ามเปลี่ยนชื่อหรือโค้ดข้างในไฟล์ account-service.json หรือ .gitignore เด็ดขาด
### ห้าม commit account-service.json เป็นอันเด็ดขาด!!!!!!!!!

# How to install libraries
ต้องมี Python v3.9 ขึ้นไปพร้อมลงใน PATH
```
cd myproject
```
ลง venv & library ที่ต้องใช้
```
python -m venv venv
venv\Scripts\activate
pip install flask gspread oauth2client bcrypt datetime
```
โฟล์เดอร์ควรเป็นไปตามนี้
```
my-project/
├── static
│   ├── style1.css
│   ├── style2.css
│   ├── style3.css
│   └── style4.css
├── templates
│   ├── dashboard.html
│   ├── index.html
│   ├── login.html
│   └── result.html
├── venv
├── add_student.py
├── app.py
├── debugging.py
├── delete_student.py
├── init_db.py
├── README.md
├── rename_column
└── .gitignore
```
# วิธีการ Run ในเครื่อง
***รันด้วย Command Prompt (Admin)***
- เข้าถึงโฟลเดอร์ที่มีไฟล์อยู่
```
cd myproject
```
- รัน venv
```
venv\Scripts\activiate
```
- ให้ขึ้น (venv) C:\Users\myproject> แสดงว่าถูกต้อง
- python (ชื่อไฟล์).(นามสกุลไฟล์)
```
python app.py
```