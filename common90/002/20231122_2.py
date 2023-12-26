from itertools import product

N = int(input())

answer = []
for i in product([0, 1], repeat=N):
    word = ""
    is_ok = True
    open_cnt = 0
    for j in i:
        if j == 0:
            word += "("
            open_cnt += 1
        elif j == 1:
            if open_cnt == 0:
                is_ok = False
                break
            word += ")"
            open_cnt -= 1
    if is_ok:
        answer.appen(word)

answer.sort()
print(*answer, sep="\n")





