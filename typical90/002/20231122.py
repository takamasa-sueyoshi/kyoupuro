N = int(input())

answer = []
for i in range(1, 1 << N):
    open_cnt = 0
    word = ""
    is_ok = True
    for j in range(N):
        if i & 1 << j:
            word += "("
            open_cnt += 1
        else:
            if open_cnt == 0:
                is_ok = False
                break
            word += ")"
            open_cnt -= 1
    if is_ok:
        answer.append(word)

answer.sort()
print(*answer, sep="\n")



