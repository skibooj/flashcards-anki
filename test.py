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
for row in ws.rows:
    for cell in row:
        dct['%s' % cell.value] = CreateFlashcard(cell.value)

