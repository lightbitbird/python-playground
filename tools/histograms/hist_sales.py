# You need install matplotlib at first
# pip install matplotlib

from pathlib import Path
import math
import openpyxl
from matplotlib import pyplot
import os

jp_font = 'Meiryo'
pyplot.style.use('seaborn')


def xl_read(xl_path, cell_range, col_idx):
    lst = []
    wb = openpyxl.load_workbook(xl_path)
    ws = wb['Sheet1']

    for r in ws[cell_range]:
        lst.append(r[col_idx].value)

    return lst


def draw_hist_sales(sales_list, bin_edges):
    pyplot.hist(sales_list, bins=bin_edges, edgecolor='black', linewidth=1.0)
    pyplot.xlabel('Sales/Day', fontname=jp_font)
    pyplot.ylabel('Frequency', fontname=jp_font)


# read data
current_dir = os.path.dirname(__file__)
file_path = Path(current_dir + '/files/shop_sales.xlsx')
data_list = xl_read(file_path, 'B2:B32', 0)

data_max, data_min, data_n = max(data_list), min(data_list), len(data_list)
print('Max: ', data_max)
print('Min: ', data_min)
print('Number: ', data_n)
print()

print('Range: ', data_max - data_min)
print('Star jes: ', 1 + math.log2(data_n))
print()

bin_min = int(input('Lower limit of class='))
bin_max = int(input('Upper limit of class='))
bin_w = int(input('Range of class='))

# histogram
edges = range(bin_min, bin_max + bin_w, bin_w)
draw_hist_sales(data_list, edges)

pyplot.show()
