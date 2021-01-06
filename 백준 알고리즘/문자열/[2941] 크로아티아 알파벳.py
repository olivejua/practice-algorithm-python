croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

letters = input()
count = 0
# while letters:
#     if letters[0:2] in croatia:
#         letters = letters[2:]
#     elif letters[0:3] in croatia:
#         letters = letters[3:]
#     else:
#         letters = letters[1:]
#     count = count + 1
#
# print(count)

for i in croatia:
    count += letters.count(i)
print(len(letters) - count)

for i in croatia:
    if i in letters:
        letters = letters.replace(i, '.')
print(len(letters))