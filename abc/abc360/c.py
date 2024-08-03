n = int(input())
a = list(map(int, input().split()))
w = list(map(int, input().split()))

box = [0] * (n + 1)
for i in range(n):
    box[a[i]] = max(box[a[i]], w[i])

print(sum(w) - sum(box))
