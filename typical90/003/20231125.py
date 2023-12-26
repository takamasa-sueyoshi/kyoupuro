from queue import Queue

N = int(input())
ROUTE_NUM = N - 1

G = [[] for _ in range(N)]
for i in range(ROUTE_NUM):
    A, B = map(lambda x: int(x) - 1, input().split())
    G[A].append(B)
    G[B].append(A)


def dikstra(s, g):
    dist = [-1] * N
    dist[s] = 0
    Q = Queue()
    Q.put(s)
    while not Q.empty():
        current = Q.get()
        for next in g[current]:
            if dist[next] >= 0:
                continue
            dist[next] = dist[current] + 1
            Q.put(next)
    return dist


dist_from_zero = dikstra(0, G)
dist_from_max = dikstra(dist_from_zero.index(max(dist_from_zero)), G)

print(max(dist_from_max) + 1)
