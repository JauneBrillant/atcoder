n = int(input())


def f(num):
    pair = []
    for a in range(1, int(num**0.5) + 1):
        if num % a == 0:
            b = num // a
            pair.append((a, b))
            pair.append((b, a))
    return len(set(pair))


ans = 0
for x in range(1, n):
    y = n - x
    if y <= 0:
        continue
    ans += f(x) * f(y)

print(ans)
