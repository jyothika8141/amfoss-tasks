def max_prime_fact(n):
    global maxprime
    while n % 2 == 0:
        maxprime = 2
        n //= 2
    for i in range(n, 2, -2):
        if n % i == 0:
            for j in range(3, i//2, 2):
                if i % j == 0:
                    break
            else:
                maxprime = i
                break
    return maxprime


t = int(input().strip())
for a0 in range(t):
    x = int(input().strip())
    print(max_prime_fact(x))
