N = int(input())

# 奇数個しかない場合は成立しない
if N % 2 != 0:
    exit()

answer = []

for i in range(1, 1 << N):
    word = ""
    open_count = 0
    for j in range(N):
        if i & 1 << j:
            if open_count > 0:
                word += ")"
                open_count -= 1
            else:
                break
        else:
            word += "("
            open_count += 1
    if len(word) == N and open_count == 0:
        answer.append(word)

answer.sort()
print(*answer, sep="\n")



