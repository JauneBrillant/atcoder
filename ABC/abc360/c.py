from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
w = list(map(int, input().split()))

hashmap = defaultdict(list)
for i in range(n):
    hashmap[a[i]].append(w[i])

for key in hashmap:
    hashmap[key].sort(reverse=True)

ans = 0
for k, v in hashmap.items():
    while len(v) > 1:
        ans += v.pop()

print(ans)
