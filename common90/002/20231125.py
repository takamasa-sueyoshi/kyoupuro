N = int(input())

if N % 2 != 0:
    exit()

answer = []
# 2のN乗個の0・1パターンを検証する
for pattern in range(1, 1 << N):
    open_cnt = 0
    word = ""
    # その0・1パターンについて、各桁をチェック
    for j in range(N):
        # 1であれば「)」と見なす
        if pattern & 1 << j:
            # 左から並べて行った時に、「)」が「(」より多くなることはない
            if open_cnt > 0:
                open_cnt -= 1
                word += ")"
            # 例外はパターンとして成り立たない
            else:
                break
        else:
            open_cnt += 1
            word += "("
    else:
        # 例外が見つからず、「(」と「)」が同じ数だけ存在する場合は正しいパターン
        if word.count("(") == N // 2:
            answer.append(word)

answer.sort()
print(*answer, sep="\n")
