n = int(input())
s = input()

sequence = s.split("-")
ans = 1
for seq in sequence:
    ans = max(ans, len(seq))

print(-1 if all(ch == s[0] for ch in s) else ans)
