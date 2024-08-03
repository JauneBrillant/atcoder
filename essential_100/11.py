n, m = map(int, input().split())
rights = []
for _ in range(m):
    s = list(map(int, input().split()))
    rights.append(s[1:])
p = list(map(int, input().split()))

ans = 0
for bit in range(1 << n):
    switch = [False] * n
    for i in reversed(range(n)):
        if bit >> i & 1:
            switch[i] = True

    for i, right in enumerate(rights):
        cnt = 0
        for j in right:
            if switch[j - 1]:
                cnt += 1
        if cnt % 2 != p[i]:
            break
    else:
        ans += 1

print(ans)
