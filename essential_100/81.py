N = int(input())
M = 10**6 + 9
acc = [0] * M

for _ in range(N):
    l, r = map(int, input().split())
    acc[l] += 1
    acc[r + 1] -= 1

for i in range(M):
    acc[i] += acc[i - 1]

print(max(acc))
