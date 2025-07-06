import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('rwb-sb-account-db-da8565c59ec7.json', scope)
client = gspread.authorize(creds)

# ✅ Use correct worksheet name
sheet = client.open('RWB-SR Student Database').worksheet("Sheet1")  # Change if needed

# ✅ Update a known cell
sheet.update_cell(2, 8, "999")  # Row 2, column H
print("Updated successfully")
