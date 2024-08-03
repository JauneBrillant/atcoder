n = int(input())
a = list(map(int, input().split()))
aa = sorted(set(a), reverse=True)

hashmap = {}
cnt = 0
for num in aa:
    hashmap[num] = cnt
    cnt += 1

ans = [0] * n
for e in a:
    ans[hashmap[e]] += 1
print(*ans)
