h, w = map(int, input().split())
ss = []
for _ in range(h):
    s = list(input())
    ss.append(s)

for s in ss:
    j = 0
    while j < w - 1:
        if s[j] == s[j + 1] == "T":
            s[j] = "P"
            s[j + 1] = "C"
            j += 2
        else:
            j += 1

for s in ss:
    print("".join(s))
