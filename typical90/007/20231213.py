N = int(input())
A = list(map(int, input().split()))
Q = int(input())

INF = 10 ** 10

def lower_bound(array, key):
    begin = -1
    end = len(array)
    while end - begin > 1:
        mid = (begin + end) // 2
        if key >= A[mid]:
            begin = mid
        else:
            end = mid
    return end

A.sort()

for _ in range(Q):
    B = int(input())
    pos = lower_bound(A, B)
    diff_a = diff_b = INF
    if pos >= 1:
        diff_a = abs(A[pos - 1] - B)
    if pos <= N - 1:
        diff_b = abs(A[pos] - B)
    print(min(diff_a, diff_b))