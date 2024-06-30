s, t = input().split()

ok = False
for w in range(1, len(s)):
    for c in range(w):
        if s[c::w] == t:
            ok = True

print("Yes" if ok else "No")
