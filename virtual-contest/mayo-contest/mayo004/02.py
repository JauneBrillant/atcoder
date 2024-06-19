def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


a, b, c, d = map(int, input().split())

win = "Aoki"
for i in range(a, b + 1):
    if all(not is_prime(i + j) for j in range(c, d + 1)):
        win = "Takahashi"
        break

print(win)
