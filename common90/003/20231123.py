from queue import Queue

# 都市の数
N = int(input())

# 隣接リスト
G = [[] for i in range(N)]
for i in range(N - 1):
    A, B = map(lambda x: int(x) - 1, input().split())
    G[A].append(B)
    G[B].append(A)


# 木の直径を求める関数
def get_tree_diameter(start, adjacency_list):
    # キューの作成。探索する都市番号をキューに追加していく
    Q = Queue()
    # 起点からの距離を記録するリスト
    dist = [-1] * N
    # まずは起点自身の探索。距離はもちろん0。
    dist[start] = 0
    # 探索が必要な都市が無くなるまで処理を続ける
    Q.put(start)
    while not Q.empty():
        current = Q.get()
        # 探索対象の都市と隣り合う都市について以下処理
        for next in adjacency_list[current]:
            # 距離が0以上なら探索済みなのでスキップ
            if dist[next] >= 0:
                continue
            # 探索対象の都市より距離が1大きくなる
            dist[next] = dist[current] + 1
            # キューに含める
            Q.put(next)
    return dist


# 都市1を起点とした各都市までの距離を取得
dist_from_zero = get_tree_diameter(0, G)
# 都市1から最も遠く離れた都市を取得
max_tree_diameter_index = dist_from_zero.index(max(dist_from_zero))

# 解答
answer = max(get_tree_diameter(max_tree_diameter_index, G)) + 1
print(answer)
