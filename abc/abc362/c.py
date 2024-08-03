n = int(input())
l = []
r = []
for i in range(n):
    li, ri = map(int, input().split())
    l.append(li)
    r.append(ri)

curr_sum = sum(l)
if curr_sum > 0:
    print("No")
    exit()

res = [num for num in l]
for i in range(n):
    add = min(0 - curr_sum, r[i] - l[i])
    res[i] += add
    curr_sum += add

if sum(res) == 0:
    print("Yes")
    print(*res)
else:
    print("No")
