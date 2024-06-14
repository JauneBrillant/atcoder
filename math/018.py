n = int(input())
a = list(map(int, input().split()))

print(a.count(100) * a.count(400) + a.count(200) * a.count(300))
