from collections import defaultdict

n = int(input())
x, y = [], []
for _ in range(n):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)
s = input()

hashmap = defaultdict(list)
for i in range(n):
    if s[i] == "L":
        hashmap[y[i]].append((1, x[i]))
    else:
        hashmap[y[i]].append((0, x[i]))

ok = False
for lst in hashmap.values():
    lst.sort()
    if (
        lst[0][0] == 0
        and lst[len(lst) - 1][0] == 1
        and lst[0][1] < lst[len(lst) - 1][1]
    ):
        ok = True
        break

print("Yes" if ok else "No")
