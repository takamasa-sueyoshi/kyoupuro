from itertools import product

N = int(input())

if N % 2 != 0:
    exit()

answer = []
for pattern in product([0, 1], repeat=N):
    if pattern.count(0) != N//2:
        continue
    open_cnt = 0
    word = ""
    is_ok_pattern = True
    for element in pattern:
        if element == 0:
            open_cnt += 1
            word += "0"
        else:
            open_cnt -= 1
            if open_cnt < 0:
                is_ok_pattern = False
                break
            word += "1"
    if is_ok_pattern:
        replaced_word = word.replace("0", "(").replace("1", ")")
        answer.append(replaced_word)

answer.sort()
print(*answer, sep="\n")



