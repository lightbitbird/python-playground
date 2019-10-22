import datetime
import openpyxl
import os

current_dir = os.path.dirname(__file__)
xlsx_file = current_dir + '/members.xlsx'
text_file = current_dir + '/validmembers.txt'

id_list = []
now = datetime.datetime.now()
prev = now + datetime.timedelta(days=180)

# excel book
wb = openpyxl.load_workbook(xlsx_file, data_only=True)

# excel sheet
ws = wb["Sheet1"]

for row in ws.iter_rows(min_row=2):
    member_id = row[0].value
    member_name = row[1].value
    expire_date = row[3].value

    # filter a range of dates in 180 days
    if now <= expire_date <= prev:
        id_list.append([member_id, member_name])

id_list.sort()

with open(text_file, "w") as f:
    for i in id_list:
        f.write(str(i[0]) + "," + i[1] + "\n")
