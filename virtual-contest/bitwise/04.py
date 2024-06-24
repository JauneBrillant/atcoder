N, M, K = map(int, input().split())
A = []
R = []
for _ in range(M):
    line = input().split()
    A.append(list(map(int, line[1:-1])))
    R.append(line[-1])

for bit in range(1 << N):
    ok = True
    for i in range(N):
        if bit & (1 << i):
            
