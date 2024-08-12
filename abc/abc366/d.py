from tabulate import tabulate

N = int(input())
A = [[[0] * (N + 2) for _ in range(N + 2)] for _ in range(N + 2)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        A[i][j][1 : N + 1] = map(int, input().split())
Q = int(input())


for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            A[i][j][k] += A[i - 1][j][k]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            A[i][j][k] += A[i][j - 1][k]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            A[i][j][k] += A[i][j][k - 1]


print(tabulate(A))
for _ in range(Q):
    lx, rx, ly, ry, lz, rz = map(int, input().split())
    ans = (
        A[rx][ry][rz]
        - A[lx - 1][ry][rz]
        - A[rx][ly - 1][rz]
        - A[rx][ry][lz - 1]
        + A[lx - 1][ly - 1][rz]
        + A[lx - 1][ry][lz - 1]
        + A[rx][ly - 1][lz - 1]
        - A[lx - 1][ly - 1][lz - 1]
    )
    print(ans)
