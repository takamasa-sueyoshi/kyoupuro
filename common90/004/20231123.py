H, W = map(int, input().split())

rows = []
for _ in range(H):
    row = list(map(int, input().split()))
    rows.append(row)

row_scores = []
column_scores = [0] * W
for row in rows:
    row_scores.append(sum(row))
    for index, column in enumerate(row):
        column_scores[index] += column

scores = []
for i in range(H):
    for j in range(W):
        total = row_scores[i] + column_scores[j] - rows[i][j]
        scores.append(total)
    print(*scores)
    scores = []
