s = input()
n = len(s)

ans = 0
digit = 1
for i in reversed(range(n)):
    ans += (ord(s[i]) - ord("A") + 1) * digit
    digit *= 26

print(ans)
