n, m = map(int, input().split())
ss = []
for _ in range(m):
    line = input().split()
    ss.append(list(map(int, line[1:])))
p = list(map(int, input().split()))

ans = 0
for bit in range(1 << n):
    ok = True
    for i, s in enumerate(ss):
        on_cnt = 0
        for j in s:
            if bit >> (j - 1) & 1:
                on_cnt += 1
        if p[i] != on_cnt % 2:
            ok = False
            break
    if ok:
        ans += 1

print(ans)
