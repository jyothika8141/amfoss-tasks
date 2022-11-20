lst = []
group = input()
num_chld = input()
rm_space = num_chld.split()
for k in rm_space:
    lst.append(int(k))

num_uber = 0
dict_lst = {1: lst.count(1),
            2: lst.count(2),
            3: lst.count(3),
            4: lst.count(4)}

num_uber += dict_lst[4]
dict_lst.pop(4)

if dict_lst[2] % 2 == 0:
    num_uber += dict_lst[2]/2
    dict_lst[2] = 0
else:
    num_uber += (dict_lst[2]-1)/2
    dict_lst[2] = 1

if dict_lst[3] > dict_lst[1]:
    num_uber += dict_lst[3]
    dict_lst.pop(1)
    dict_lst.pop(3)

elif dict_lst[3] < dict_lst[1]:
    num_uber += dict_lst[3]
    dict_lst[1] -= dict_lst[3]
    dict_lst.pop(3)
    if dict_lst[1] >= 4:
        num_uber += dict_lst[1]//4
        dict_lst[1] = dict_lst[1] % 4
    if dict_lst[1] in [1,2]:
        if dict_lst[2] == 1:
            num_uber += 1
            dict_lst[2] = 0
            dict_lst.pop(1)
        else:
            num_uber +=1
    elif dict_lst[1] == 3:
        num_uber += 1
        dict_lst.pop(1)

elif dict_lst[3] == dict_lst[1]:
    num_uber += dict_lst[1]
    dict_lst.pop(1)
    dict_lst.pop(3)

if dict_lst[2] == 1:
    num_uber += 1
    dict_lst.pop(2)

print(int(num_uber))
