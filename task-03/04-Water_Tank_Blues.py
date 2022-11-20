amt = []
amt2 = []
lst2 = []

storage = int(input())
for m in range(storage):
    tank = int(input())
    water = input()
    rm_space = water.split()
    for k in rm_space:
        amt.append(int(k))
    amt2.append(amt)
    amt = []


for lst in amt2:
    for i in lst:
        lst2.append(i)
    for ele in lst:
        if ele == 0:
            lst2.remove(0)
        elif ele != 0:
            break
    if len(lst2) > 0:
        lst2.pop()
        freq = lst2.count(0)
        sum1 = sum(lst2)
        ans = sum1 + freq
        print(ans)
    else:
        print(0)
        
    lst2 = []
