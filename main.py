import os
from openpyxl import load_workbook
from flashcard import *
from exportExcel import export_to_excel

# set input path
os.chdir(r"/home/skibojq/projects/flashcards-anki/files")
wb = load_workbook('./input1.xlsx')
ws = wb.active

# create dictionary with words
dct = {}
print("1")
for row in ws.rows:
    for cell in row:
        try:
            dct['%s' % cell.value] = CreateFlashcard(cell.value)
        except:
            pass
print("2")
# remove unnecessery element
for n in range(0, 10):
    for x in dct.keys():
        for i in dct[x]:
            if len(i) == 1:
                del dct[x][dct[x].index(i)]

print("3")
# export to excel
export_to_excel(dct)

print("finish")
