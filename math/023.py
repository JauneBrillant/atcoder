n = int(input())
b = list(map(int, input().split()))
r = list(map(int, input().split()))

ans = (sum(b) + sum(r)) / n
print(ans)
