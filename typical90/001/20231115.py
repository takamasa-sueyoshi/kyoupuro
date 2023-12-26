# https://github.com/E869120/kyopro_educational_90/blob/main/editorial/001.jpg
# https://qiita.com/Chunky_RBP_chan/items/9ae8994fb233cde0ab5b
# https://github.com/ryusuke920/kyopro_educational_90_python/blob/main/solve_python/001.py
# キーワード：二分探索法、貪欲法
N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

A.append(L)
dif = [A[0]]
for i in range(N):
    dif.append(A[i + 1] - A[i])

# 探索範囲
ok = -1
ng = L


def is_ok(target_length):
    sliced_number = 0
    prev_length = 0
    # 羊羹を一つずつチェック。決定した長さ以上かどうか。足りなければ次の羊羹の長さを足し合わせる
    for position in A:
        length = position - prev_length
        if length >= middle:
            sliced_number += 1
            prev_length = position
    return sliced_number > K


while ok - ng > 1:
    # 何cm以上で区切るか決定する（二分探索を用いるので、探索範囲の中央とする）
    middle = (ok + ng) // 2
    if is_ok(middle):
        ok = middle
    else:
        ng = middle

print(ok)
