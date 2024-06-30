s, t = input().split()

n = len(s)
m = len(t)

ok = False
for w in range(1, n):
    splits = [s[i : i + w] for i in range(0, n, w)]
    for c in range(w):
        concat_str = ""
        for st in splits:
            if c < len(st):
                concat_str += st[c]

        if concat_str == t:
            ok = True
            break

print("Yes" if ok else "No")
