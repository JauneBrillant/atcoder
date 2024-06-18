N = int(input())

originals = {}
ans_v = 0
ans = 0

for i in range(N):
    s, tt = map(str, input().split())
    t = int(tt)

    if s not in originals:
        originals[s] = t
        if t > ans_v:
            ans_v = t
            ans = i

print(ans + 1)
