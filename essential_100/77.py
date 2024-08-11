N, M = map(int, input().split())
A = []  # 旅人の移動 M通り
B = []  # 旅館間の距離 N-1通り
for _ in range(N - 1):
    B.append(int(input()))
for _ in range(M):
    A.append(int(input()))

acc = [0] * N
total = 0
for i, b in enumerate(B, 1):
    total += b
    acc[i] = total
acc = [0] + acc

ans = 0
curr = 1
for a in A:
    if a > 0:
        ans += acc[curr + a] - acc[curr]
    else:
        ans += acc[curr] - acc[curr + a]
    curr += a

print(ans % 100000)
