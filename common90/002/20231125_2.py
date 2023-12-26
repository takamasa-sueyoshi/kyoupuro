from itertools import product

N = int(input())

if N % 2 != 0:
    exit()

answer = []
for i in product([0, 1], repeat=N):
    zero_cnt = 0
    word = ""
    if i.count(0) != N // 2:
        continue
    for j in i:
        if j == 0:
            zero_cnt += 1
            word += "("
        else:
            zero_cnt -= 1
            if zero_cnt >= 0:
                word += ")"
            else:
                break
    else:
        print(word)


