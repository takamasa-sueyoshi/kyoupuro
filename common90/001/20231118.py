N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

A.append(L)
YOKANS = [A[0]]
for i in range(N):
    YOKANS.append(A[i + 1] - A[i])


# print(YOKANS)

def is_ok(target_length):
    cnt = 0
    length = 0
    for yokan in YOKANS:
        length += yokan
        if length >= target_length:
            cnt += 1
            length = 0
    return cnt >= K + 1


ok = -1
ng = L
while ng - ok > 1:
    middle = (ok + ng) // 2
    if is_ok(middle):
        ok = middle
    else:
        ng = middle

print(ok)
