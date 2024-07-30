s = input()
n = len(s)

ans = 0
i = 0
while i < n:
    if i + 1 < n and s[i] == s[i + 1] == "0":
        i += 2
    else:
        i += 1
    ans += 1

print(ans)
