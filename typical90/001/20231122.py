N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

A.append(L)
YOKANS = [A[0]]
for i in range(N):
    YOKANS.append(A[i + 1] - A[i])


def is_ok(num):
    length = 0
    yokan_cnt = 0
    for i in YOKANS:
        length += i
        if length >= num:
            yokan_cnt += 1
            length = 0
    return yokan_cnt >= K + 1


ok = -1
ng = L

while ng - ok > 1:
    mid = (ok + ng) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

print(ok)
