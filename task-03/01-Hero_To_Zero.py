def chk_0(lst):
    global mana
    count_0 = lst.count(0)
    if count_0 == 0:
        return False
    else:
        for i in range(count_0):
            lst.remove(0)
        mana += len(lst)
        return True



def repeat(lst):
    global mana
    set1 = set(lst)
    for i in set1:
        if lst.count(i) >= 2:
            index = lst.index(i)  
            lst[index] = 0
            mana += 1
            chk_0(lst)
            return True


def no_repeat(lst):
    global mana
    _min = min(lst)
    _max = max(lst)
    index_max = lst.index(_max)
    lst[index_max] = _min
    mana += 1
    repeat(lst)


lst = []
lst1 =[]
lst2 = []

city = int(input())
for i in range(city):
    heros = int(input())
    level = input()
    rm_space = level.split()
    for k in rm_space:
        lst2.append(int(k))
    lst1 = list(lst2)
    lst2 = []
    lst.append(lst1)

for sublist in lst:
    mana = 0
    ans1 = chk_0(sublist)
    if ans1 == True:
        print(mana)
    else:
        ans2 = repeat(sublist)
        if ans2 == True:
            print(mana)
        else:
            no_repeat(sublist)
            print(mana)
