n = int(input())
a = list(map(int, input().split()))

ans = int(1 << 30)
for bit in range(1 << n - 1):
    xor = 0
    o = 0
    for i in range(n):
        o |= a[i]
        if bit & (1 << i):
            xor ^= o
            o = 0
    xor ^= o
    ans = min(ans, xor)

print(ans)
