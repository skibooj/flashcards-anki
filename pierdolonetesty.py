import urllib.request
import urllib.parse
import os
import pandas as pd
from openpyxl import load_workbook
from flashcard_dev import *

os.chdir(r"E:\inne\ang")
file = 'test.xlsx'
xl = pd.ExcelFile(file)
df1 = xl.parse('Arkusz1')

wb = load_workbook('./test.xlsx')
ws = wb.active

dct = {}
aaa = ['word', 'fly', 'stay']

for row in ws.rows:
    for cell in row:
        print(cell.value)
        #dct['%s' % cell.value] = CreateFlashcard(cell.value)

print(CreateFlashcard('bird'))

result = []


# dziala ale na poczatku trzeba zrobic w petli kilka razy
# for b in range(0,10):
#     for x in dct.keys():
#         y = 0
#         for i in dct[x]:
#             if len(i)== 1:
#                 del dct[x][y]
#             y += 1

# print (dct)
# for x in dct.keys():
#     print(x)
#     for i in dct[x]:
#         print(dct[x][dct[x].index(i)])#

# if len(i) == 1:
#     del dct[x][dct[x].index(i)]
