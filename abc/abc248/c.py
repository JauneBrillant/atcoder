# dp[i][j] := 数列の先頭からi項目まで決めた際に、総和がjであるような数列の決め方の総和

n, m, k = map(int, input())
dp = [[0] * k for _ in range(n)]

for i in range(n):
    for j in range(k):
        
