from bisect import bisect_right

full_length = int(input())
n = int(input())
m = int(input())
store = [0]
destination = []
for _ in range(n - 1):
    store.append(int(input()))
for _ in range(m):
    destination.append(int(input()))
store.sort()


ans = 0
for ds in destination:
    pos = bisect_right(store, ds)

    if pos == n:
        ans += min(ds - store[-1], full_length - ds)
    else:
        ans += min(ds - store[pos - 1], store[pos] - ds)

print(ans)
