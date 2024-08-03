n, a = map(int, input().split())
tt = list(map(int, input().split()))

pre = 0
for t in tt:
    pre = max(t, pre) + a
    print(pre)
