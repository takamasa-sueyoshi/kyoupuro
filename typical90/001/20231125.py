N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

A.append(L)

yokans = [A[0]]
for i in range(N):
    yokans.append(A[i + 1] - A[i])


def is_cut_ok(cut_length):
    length = 0
    cut_cnt = 0
    for yokan in yokans:
        length += yokan
        if length >= cut_length:
            cut_cnt += 1
            length = 0
    return cut_cnt >= K + 1


ok = -1
ng = L
while ng - ok > 1:
    mid = (ok + ng) // 2
    if is_cut_ok(mid):
        ok = mid
    else:
        ng = mid

print(ok)
