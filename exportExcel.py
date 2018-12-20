import os
import xlsxwriter


def export_to_excel(dictionary):
    # set directory path
    os.chdir(r"/home/skibojq/projects/flashcards-anki/output")
    workbook = xlsxwriter.Workbook('out.xlsx')
    worksheet = workbook.add_worksheet('Flashcards')

    # exporting to excel
    row = 0
    col = 0
    for key in dictionary:
        row += 1
        worksheet.write(row, col, key)
        i = 0
        for item in dictionary[key]:
            worksheet.write(row, col + i, item)  # add all element from list
            i += 1

    workbook.close()
