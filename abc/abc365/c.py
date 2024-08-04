N, M = map(int, input().split())
A = list(map(int, input().split()))

# 交通費支給額の上限を儲けることはしなくても（全員に交通費を満額支給しても）予算以内の場合（M以下の場合）
if sum(A) <= M:
    print("infinite")
    exit()


def cond(x):
    total_cost = sum(min(a, x) for a in A)
    return total_cost <= M


# 交通費支給額の上限の範囲を二分探索して、トータルの出費が予算以下(M)になる範囲を調べる
# ok : 交通費支給額上限が0円だと、一円もコストがかからないので確実に条件を満たす (total_cost <= M)
# ng : 交通費支給額上限を一番交通費がかかる人にすると(全員に交通費をを満額支給)、予算(M)をオーバーするのでNG (sum(A) <= M でないことを既に確認済み)
ok, ng = 0, max(A)
while ok + 1 < ng:
    mi = (ok + ng) // 2
    if cond(mi):
        ok = mi
    else:
        ng = mi

print(ok)
