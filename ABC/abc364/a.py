n = int(input())
s = [input() for _ in range(n)]

ok = True
for i in range(n - 2):
    if s[i] == s[i + 1] == "sweet":
        ok = False

print("Yes" if ok else "No")
