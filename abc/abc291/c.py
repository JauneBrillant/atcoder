n = int(input())
s = input()

visited = set()
i, j = 0, 0
ok = False
for c in s:
    visited.add((i, j))

    if c == "R":
        i += 1
    if c == "L":
        i -= 1
    if c == "U":
        j += 1
    if c == "D":
        j -= 1

    if (i, j) in visited:
        ok = True
        break

print("Yes" if ok else "No")
