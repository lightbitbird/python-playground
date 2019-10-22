import os
import csv

current_dir = os.path.dirname(__file__)
stores_path = current_dir + "/store_code.csv"

with open(stores_path, encoding="utf-8") as f:
    reader = csv.reader(f)
    # next(reader)
    for row in reader:
        folder_name = row[0] + '_' + row[1]
        print(folder_name)
        if not os.path.exists(folder_name):
            os.mkdir(current_dir + '/' + folder_name)
