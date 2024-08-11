N = int(input())
A = []
for _ in range(N):
    M = int(input())
    xy = []
    for _ in range(M):
        x, y = map(int, input().split())
        xy.append((x, y))
    A.append(xy)

ans = 0
for bit in range(1 << N):
    ok = True
    for i in range(N):
        if bit & 1 << i:
            for x, y in A[i]:
                if y == 1 and not (bit & 1 << (x - 1)):
                    ok = False
                    break
                if y == 0 and (bit & 1 << (x - 1)):
                    ok = False
                    break
            if not ok:
                break
    else:
        ans = max(ans, bin(bit).count("1"))

print(ans)
