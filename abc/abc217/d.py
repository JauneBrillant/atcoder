from sortedcontainers import SortedSet

L, Q = map(int, input().split())
st = SortedSet()
st.add(0)
st.add(L)

for _ in range(Q):
    c, x = map(int, input().split())
    match c:
        case 1:
            st.add(x)
        case 2:
            i = st.bisect(x)
            print(st[i] - st[i - 1])
