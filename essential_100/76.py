N = int(input())
A = list(map(int, input().split()))

acc = [0] * (N + 1)
total = 0
for i, a in enumerate(A, 1):
    total += a
    acc[i] = total


for k in range(N):
    mx = 0
    for i in range(1 + k, N + 1):
        mx = max(mx, acc[i] - acc[i - k - 1])
    print(mx)
