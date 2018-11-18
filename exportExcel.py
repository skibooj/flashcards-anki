import os
import xlsxwriter


def export_to_excel(file):
    # set directory path
    os.chdir(r"/home/skibojq/projects/flashcards-anki/output")
    workbook = xlsxwriter.Workbook('out.xlsx')
    worksheet = workbook.add_worksheet('Flashcards')

    # export to excel
    dictionary = file
    row = 0
    col = 0
    for key in dictionary.keys():
        row += 1
        worksheet.write(row, col, key)
        for item in dictionary[key]:
            for i in range(1, 10):
                try:
                    worksheet.write(row, col + i, item[i - 1])
                except:
                    pass

    workbook.close()
