n = int(input())
lst = []

for i in range(n):
    x = int(input())
    lst.append(x)


for ele in lst:
    i = 0
    j = 1
    k = 0
    sum = 0
    while k < ele:
        k = i+j
        if k % 2 == 0 and k < ele:
            sum += k
        i = j
        j = k
    print(sum)
