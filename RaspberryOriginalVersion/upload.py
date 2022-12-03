import gspread
from oauth2client.service_account import ServiceAccountCredentials

def upload(total_person, values):
    i = 1
    while (i <= (len(values))):
    #for i in range(1,len(values)+1):                  
        sheet.update_cell(str(total_person), i, values[i-1])
        i+=1

scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]
## testdatacamera@testproject-369413.iam.gserviceaccount.com
credentials = ServiceAccountCredentials.from_json_keyfile_name('upload.json', scope)
client = gspread.authorize(credentials)
sheet = client.open('EVENTO SOBREMESA')
sheet = sheet.get_worksheet(1)


