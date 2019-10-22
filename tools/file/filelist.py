import os
import csv
import time

# csv_file = './file_list.csv'
current_dir = os.path.dirname(__file__)
list_dir = current_dir + '/files'
csv_file = current_dir + '/file_list.csv'
date_format = '%Y/%m/%d %H:%M:%S'

file_list = []

for file in os.listdir(list_dir):
    fpath = list_dir + '/' + file
    is_file = os.path.isfile(fpath)
    # if is a python file itself or not
    not_py_file = os.path.basename(__file__) != file
    not_csv_file = csv_file != fpath

    if is_file and not_py_file and not_csv_file:
        # extension
        ext = os.path.splitext(file)[1]
        # last accessed time
        accessed_time = time.strftime(
            date_format, time.localtime(os.path.getatime(fpath)))
        # created time
        time_crt = time.strftime(
            date_format, time.localtime(os.path.getctime(fpath)))
        # updated time
        time_mod = time.strftime(
            date_format, time.localtime(os.path.getmtime(fpath)))
        # full path
        path = os.path.abspath(fpath)
        # size
        size = os.path.getsize(fpath)
        file_list.append([file, ext, accessed_time,
                          time_crt, time_mod, path, size])

with open(csv_file, "w", newline="") as f:
    csv_writer = csv.writer(f)
    for r in file_list:
        csv_writer.writerow(r)
