n, k = map(int, input().split())
a = list(map(int, input().split()))

group = []
for i in range(k):
    group.append(sorted(a[i::k]))

ok = True
prev = 0
for gp in zip(*group):
    for num in gp:
        if num < prev:
            ok = False
        prev = num

print("Yes" if ok else "No")
