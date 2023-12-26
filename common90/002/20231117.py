from itertools import product

N = int(input())

if N % 2 != 0:
    exit()

answer = []

for pattern in product(["(", ")"], repeat=N):
    if pattern.count("(") != pattern.count(")"):
        continue
    open_count = 0
    is_ok_pattern = True
    for element in pattern:
        if element == "(":
            open_count += 1
        elif open_count == 0:
            is_ok_pattern = False
            break
        else:
            open_count -= 1
    if is_ok_pattern:
        answer.append("".join(pattern))

answer.sort()
print(*answer, sep="\n")

