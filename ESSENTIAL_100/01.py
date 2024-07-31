def solve(n, x):
    res = 0
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            for c in range(b + 1, n + 1):
                if a + b + c == x:
                    res += 1
    return res


while True:
    n, x = map(int, input().split())
    if n == x == 0:
        break
    print(solve(n, x))
