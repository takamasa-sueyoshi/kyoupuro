def lower_bound(array, key):
    begin = -1
    end = len(array)
    while end - begin > 1:
        mid = (begin + end) // 2
        target = array[mid]
        if target >= key:
            end = mid
        else:
            begin = mid
    return end

INF = 2000000000
N = int(input())
A = list(map(int, input().split()))
Q = int(input())

# 点数の低い順に並んでいる（点数昇順）
A.sort()

for i in range(Q):
    B_item = int(input())
    pos = lower_bound(A, B_item)
    ans_a = abs(A[pos] - B_item) if pos < N else INF
    ans_b = abs(A[pos - 1] - B_item) if pos >= 1 else INF
    print(min(ans_a, ans_b))
