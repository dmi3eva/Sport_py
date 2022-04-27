import sys
sys.setrecursionlimit(2000)


def generate_cbs(n, open_amount, close_amount, current):
    if open_amount == n and close_amount == n:
        print(current)
        return
    if open_amount < n:
        generate_cbs(n, open_amount+1, close_amount, current+"(")
    if close_amount < open_amount:
        generate_cbs(n, open_amount, close_amount+1, current + ")")


n = int(input())
generate_cbs(n, 0, 0, "")