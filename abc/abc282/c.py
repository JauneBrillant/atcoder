n = int(input())
s = input()

i = 0
ans = ""
while i < n:
    if s[i] == '"':
        pos = s.find('"', i + 1)
        ans += s[i : pos + 1]
        i += pos - i + 1
    else:
        ans += s[i].replace(",", ".")
        i += 1

print(ans)
