n = int(input())
p = list(map(int, input().split()))

cnt = [0] * n
for i in range(n):
    j = (p[i] - i) % n
    cnt[(j - 1) % n] += 1
    cnt[j % n] += 1
    cnt[(j + 1) % n] += 1

print(max(cnt))
