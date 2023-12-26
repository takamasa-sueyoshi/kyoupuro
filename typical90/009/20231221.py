N = int(input())

G = [[0, 0] for _ in range(N)]
for i in range(N):
    G[i][0], G[i][1] = map(int, input().split())

print(G)

