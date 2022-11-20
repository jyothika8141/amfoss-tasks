def open_portal(lst, n):
    global count
    key_x = lst[n-1]
    count += 1
    if key_x == 0:
        return count
    else:
        open_portal(portal, key_x)


count = 0
lst = []
key_lst = []
portal_lst = []

testcases = int(input())
for i in range(testcases):
    key_num = int(input())
    key_lst.append(key_num)
    ans = input()
    rm_space = ans.split()
    for k in rm_space:
        lst.append(int(k))
    portal_lst.append(lst)
    lst = []

for key, portal in zip(key_lst,portal_lst):
    open_portal(portal, key)
    if count == 3:
        print("YES")
    else:
        print("NO")
    count = 0
