N, M = map(int, input().split())
A = list(map(int, input().split()))


def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    if n > 2:
        factors.append(n)

    return set(factors)


ans = []
prime_st = set()
for a in A:
    prime_st |= prime_factors(a)

for k in range(1, M + 1):
    for v in prime_factors(k):
        if v in prime_st:
            break
    else:
        ans.append(k)

print(len(ans))
print(*ans)
