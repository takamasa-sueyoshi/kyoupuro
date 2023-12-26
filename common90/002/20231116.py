from itertools import product
N = int(input())

if N % 2 != 0:
    exit()

answer = []

for i in product([0, 1], repeat=N):
    if i.count(0) != i.count(1):
        continue
    zero_cnt = 0
    bin_string = ""
    is_ok = True
    for j in i:
        if j == 0:
            zero_cnt += 1
        else:
            if zero_cnt == 0:
                is_ok = False
                break
            else:
                zero_cnt -= 1
        bin_string += str(j)

    if is_ok:
        x = bin_string.replace("0", "(")
        y = x.replace("1", ")")
        answer.append(y)

answer.sort()
print(*answer, sep="\n")



