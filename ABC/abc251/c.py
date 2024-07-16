n = int(input())

originals = {}
for i in range(n):
    s, t = input().split()
    if s not in originals:
        originals[s] = (i, int(t))

ans = (-1, -1)
for i, t in originals.values():
    if t > ans[1] or (t == ans[1] and i < ans[0]):
        ans = (i, t)

print(ans[0] + 1)
