from collections import defaultdict

n, k = map(int, input().split())
s = [input() for _ in range(n)]

ans = 0
for bit in range(1 << n):
    hashmap = defaultdict(int)
    for i in range(n):
        if bit & (1 << i):
            for c in s[i]:
                hashmap[c] += 1
    pos = 0
    for v in hashmap.values():
        if v == k:
            pos += 1

    ans = max(ans, pos)

print(ans)
