def prime_factorization(n):
    prime_factors = []
    while n % 2 == 0:
        n = n / 2
        prime_factors.append(2)
    for i in range(3, int(n**0.5 + 1), 2):
        while n % i == 0:
            n = n / i
            prime_factors.append(i)
    if n > 2:
        prime_factors.append(int(n))
    return prime_factors


lst =[]
lst1 = []
ans = input()
rm_space = ans.split()
for k in rm_space:
    lst1.append(int(k))
n = lst1[0]
m = lst1[1]


if m % n == 0:
    x = int(m/n)
    if x == 1:
        print(0)
    else:
        prime_lst = prime_factorization(x)
        for ele in prime_lst:
            if ele not in [2, 3]:
                print(-1)
                exit()
        round = len(prime_lst)
        print(round)
else:
    print(-1)
