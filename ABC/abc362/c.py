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
    if curr_sum - l[i] + r[i] < 0:
        res[i] = r[i]
        curr_sum += -l[i] + r[i]
    else:
        res[i] += abs(curr_sum)
        break

if sum(res) == 0:
    print("Yes")
    print(*res)
else:
    print("No")
