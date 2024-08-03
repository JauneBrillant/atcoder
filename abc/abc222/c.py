def gcp(one, two, i, j):
    if one == two:
        return -1

    match one:
        case "G":
            if two == "C":
                return 0
            else:
                return 1
        case "C":
            if two == "P":
                return 0
            else:
                return 1
        case "P":
            if two == "G":
                return 0
            else:
                return 1


n, m = map(int, input().split())
a = [input() for _ in range(2 * n)]
rank = [[0, i] for i in range(2 * n)]

for round in range(m):
    for i in range(n):
        p1 = rank[2 * i][1]
        p2 = rank[2 * i + 1][1]
        res = gcp(a[p1][round], a[p2][round], p1, p2)
        if res != -1:
            rank[2 * i + res][0] -= 1
    rank.sort()

for _, i in rank:
    print(i + 1)
