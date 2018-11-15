s = {'t': [[111, 222, 333], [111, 222], [111], [333], [444], [555], [666, 777]]}
i = 0


# usuwanie zbędnych dupereli
# for x in s['t']:
#     if len(s['t'][i]) == 1:
#         del s['t'][i]
#     i += 1

for x in s:
    print(s[x])
