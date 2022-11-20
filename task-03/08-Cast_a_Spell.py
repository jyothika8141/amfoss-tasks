lst = []
lst2 = []
ini = input()
dct = {}

rm_space = ini.split()
for i in rm_space:
    lst.append(int(i))

for i in range(lst[1]):
    lang = input()
    lang2 = lang.split()
    lst2.append(lang2)

spell = input()
spell2 = spell.split()

for i in lst2:
    if len(i[0]) > len(i[1]):
        dct[i[0]] = i[1]
    else:
        dct[i[0]] = i[0]

for i in spell2:
    print(dct[i], end=" ")
