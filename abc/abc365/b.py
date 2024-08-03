n = int(input())
a = list(map(int, input().split()))

aa = []
for i in range(n):
    aa.append((a[i], i + 1))

aa.sort()
print(aa[-2][1])
