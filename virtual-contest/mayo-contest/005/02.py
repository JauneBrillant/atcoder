from collections import defaultdict

N, Q = map(int, input().split())

st = defaultdict(set)
for _ in range(Q):
    t, a, b = map(int, input().split())
    match t:
        case 1:
            st[a].add(b)
        case 2:
            st[a].discard(b)
        case 3:
            if a in st[b] and b in st[a]:
                print("Yes")
            else:
                print("No")
