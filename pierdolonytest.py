import os
import xlsxwriter

d = {'Words': [[''], ['noun', 'definition: a single distinct meaningful element of speech or writing, used with others (or sometimes alone) to form a sentence and typically shown with a space on either side when written or printed.', "example: I don't like the word ‘unofficial’"], ['adverb'], ['adjective'], ['verb', 'definition: express (something spoken or written) in particular words.', 'example: he words his request in a particularly ironic way']], 'Luckily': [[''], ['noun'], ['adverb', 'definition: it is fortunate that.', "example: luckily they didn't recognize me"], ['adjective'], ['verb']], 'exhaustive': [[''], ['noun'], ['adverb'], ['adjective', 'definition: including or considering all elements or aspects; fully comprehensive.', 'example: the guide outlines every bus route in exhaustive detail'], ['verb']], 'kinda': [[''], ['noun'], ['adverb'], ['adjective'], ['verb']], 'redo': [[''], ['noun'], ['adverb'], ['adjective'], ['verb', 'definition: do (something) again or differently.', "example: a whole day's work has to be redone"]], 'decent': [[''], ['noun'], ['adverb'], ['adjective', 'definition: conforming with generally accepted standards of respectable or moral behaviour.', 'example: a decent clean-living individual'], ['verb']], 'consider': [[''], ['noun'], ['adverb'], ['adjective'], ['verb', 'definition: think carefully about (something), typically before making a decision.', 'example: each application is considered on its merits']], 'yield': [[''], ['noun', 'definition: an amount produced of an agricultural or industrial product.', 'example: the milk yield was poor'], ['adverb'], ['adjective'], ['verb', 'definition: produce or provide (a natural, agricultural, or industrial product).', 'example: the land yields grapes and tobacco']]}

os.chdir(r"E:\inne\ang")

workbook = xlsxwriter.Workbook('.xlsx')
worksheet = workbook.add_worksheet('DUPA')
row = 0

col = 0

# for key in d.keys():
#     row += 1
#     worksheet.write(row, col, key)
#     for item in d[key]:
#         worksheet.write(row, col + 1, item)
#         row += 1

# workbook.close()

for b in range(0, 10):
    for x in d.keys():
        y = 0
        for i in d[x]:
            if len(i) == 1:
                del d[x][y]
            y += 1

for key in d.keys():
    row += 1
    ws1.write(row, col, key)
    for item in d[key]:
        ws1.write(row, col + 1, item[0])
        ws1.write(row, col + 2, item[1])
        ws1.write(row, col + 3, item[2])

workbook.close()
