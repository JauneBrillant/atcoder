n, k = map(int, input().split())
a = list(set(map(int, input().split())))
a.sort()

ans = 0
for i in range(min(k, len(a))):
    if a[i] != i:
        print(i)
        exit()

print(min(k, len(a)))
