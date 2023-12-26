N = int(input())

# 奇数個しかない場合は成立しない
if N % 2 != 0:
    exit()

MAX = N // 2


def add_r_paren(word):
    open = word.count("(")
    close = word.count(")")
    if open == MAX and close == MAX:
        print(word)
    if open < MAX:
        word += "("
        add_r_paren(word)
    if close < open:
        word += ")"
        add_r_paren(word)


add_r_paren("")
