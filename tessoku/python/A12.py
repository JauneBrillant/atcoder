n, k = map(int, input().split())
a = list(map(int, input().split()))

l = 0
r = 10**9

while l + 1 != r:
    m = (l + r) // 2
    cnt = sum(m // x for x in a)

    if cnt < k:
        l = m
    else:
        r = m

print(r)
