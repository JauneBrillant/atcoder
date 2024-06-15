def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


q = int(input())
for _ in range(q):
    x = int(input())
    print("Yes" if is_prime(x) else "No")
