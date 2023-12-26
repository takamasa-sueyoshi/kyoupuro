H, W = map(int, input().split())

rows = [list(map(int, input().split())) for _ in range(H)]

row_scores = []
column_scores = [0] * W

for row in rows:
    row_scores.append(sum(row))
    for i, column in enumerate(row):
        column_scores[i] += column

for r in range(H):
    scores = []
    for c in range(W):
        score = row_scores[r] + column_scores[c] - rows[r][c]
        scores.append(score)
    print(*scores)
