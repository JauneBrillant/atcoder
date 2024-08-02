n = int(input())


def f(x):
    cnt = 0
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            cnt += 2
            if i == x // i:
                cnt -= 1
    return cnt


ans = 0
for x in range(1, n):
    y = n - x
    ans += f(x) * f(y)

print(ans)
