def sumOfDigit(n):
    n_str = str(n)
    lst = list(n_str)
    lst2 = []
    for ele in lst:
        lst2.append(int(ele))
    return sum(lst2)

i = 0
num = int(input())
while num > 9:
    num = sumOfDigit(num)
    i += 1
print(i)
