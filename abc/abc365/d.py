n = int(input())
s = list(input())

h = []
for i in range(n):
    if s[i] == "R":
        h.append("P")
    if s[i] == "S":
        h.append("R")
    if s[i] == "P":
        h.append("S")


ans = 1
for i in range(1, n):
    if h[i] == h[i - 1]:
        h[i] == "x"

    if s[i] == "R" and h[i - 1] != "P":
        ans += 1
    elif s[i] == "S" and h[i - 1] != "R":
        ans += 1
    elif s[i] == "P" and h[i - 1] != "S":
        ans += 1

print(ans)
