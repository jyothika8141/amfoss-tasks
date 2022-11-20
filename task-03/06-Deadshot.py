num = int(input())
point = []
lst = []
count = 0

for i in range(num):
    ans = input()
    rm_space = ans.split()
    for k in rm_space:
        point.append(int(k))
    lst.append(point)
    point = []

for i in range(len(lst)):
    x_lst = []
    y_lst = []
    right = left = up = down = 0
    for point in lst:
        x_lst.append(point[0])
        y_lst.append(point[1])

    point = lst[i]
    x_lst.pop(i)
    y_lst.pop(i)

    for j in range(len(y_lst)):
        if y_lst[j] == point[1]:
            if x_lst[j] > point[0]:
                right += 1
            elif x_lst[j] < point[0]:
                left += 1

    for k in range(len(x_lst)):
        if x_lst[k] == point[0]:
            if y_lst[k] < point[1]:
                down += 1
            if y_lst[k] > point[1]:
                up += 1

    if left >= 1 and right >= 1 and down >= 1 and up >= 1:
        count += 1

print(count)
