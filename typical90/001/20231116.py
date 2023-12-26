N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

A.append(L)
diff = [A[0]]
for i in range(N):
    diff.append(A[i + 1] - A[i])


def is_ok(num):
    cnt = 0
    need_cnt = K + 1
    length = 0
    for i in diff:
        length += i
        if length >= num:
            cnt += 1
            length = 0
    if cnt >= need_cnt:
        return True
    else:
        return False


ok = -1
ng = L

while ng - ok > 1:
    m = (ng + ok) // 2
    if is_ok(m):
        ok = m
    else:
        ng = m

print(ok)
