N, M = map(int, input().split())
P = list(map(int, input().split()))
A = [0]
B = [0]
C = [0]
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)

# times[n] := 都市n~n+1間を何回移動するか
times = [0] * (N + 1)
for i in range(M - 1):
    l = min(P[i], P[i + 1])
    r = max(P[i], P[i + 1])
    times[l] += 1
    times[r] -= 1

for i in range(1, N):
    times[i] += times[i - 1]

ans = 0
for i in range(1, N):
    # print("!! " + str(i) + "番目の都市から >> " + str(i + 1) + "番目の都市に向かう")
    ticket = A[i] * times[i]
    ic = B[i] * times[i] + C[i]
    # print("回数 >> " + str(times[i]))
    # print("チケット料金 " + str(ticket) + "  IC料金 >> " + str(ic))
    ans += min(ticket, ic)

print(ans)
