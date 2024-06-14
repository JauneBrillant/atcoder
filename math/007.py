n, x, y = map(int, input().split())

sum = sum(i % x == 0 or i % y == 0 for i in range(1, n + 1))
print(sum)
