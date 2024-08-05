n, m = map(int, input().split())
s = [input() for _ in range(n)]

ans = n
for bit in range(1 << n):
    taste = [False] * m
    for i in range(n):
        if bit & 1 << i:
            for j, c in enumerate(s[i]):
                if c == "o":
                    taste[j] = True
    if all(taste):
        ans = min(ans, bit.bit_count())

print(ans)
