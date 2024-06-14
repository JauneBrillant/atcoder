n = int(input())
size = 1501

x = [[0] * size for _ in range(size)]
for _ in range(n):
    l, r = map(int, input().split())
    x[l][r] += 1

for i in range(1, size):
    for j in range(1, size):
       x[i][j] += x[i][j - 1]

for i in range(1, size):
    for j in range(1, size):
        x[j][i] += x[j - 1][i]

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    ans = x[c][d] - x[c][b - 1] - x[a - 1][d] + x[a - 1][b - 1]
    print(ans)
    
