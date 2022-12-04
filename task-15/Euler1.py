def sum(n, k):
    sum = 0
    if n % k == 0:
        div = n//k - 1
    else:
        div = n//k
    num = div*k
    div2 = div // 2
    sum += div2*(num+k) + (div%2)*((div2+1)*k)
    return sum

n = int(input())
lst = []

for i in range(n):
    x = int(input())
    lst.append(x)

for j in lst:
    sum3 = sum(j, 3)
    sum5 = sum(j, 5)
    sum15 = sum(j, 15)
    print(sum3 + sum5 - sum15)
