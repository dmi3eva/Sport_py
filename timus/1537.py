import sys
from typing import *


sys.setrecursionlimit(1000)


def count_ents(start_amount: int, k: int, p: int, height: int) -> int:
    if start_amount % p == k:
    #     from_old = count_ents(start_amount + 1, k, p, 0)
    #     from_yang = count_ents(start_amount * 2, k, p, 0)
        return 1  # + from_old + from_yang
    # if height > p:
    if start_amount > min(k, p):
        return 0
    from_old = count_ents(start_amount + 1, k, p, height + 1)
    from_yang = count_ents(start_amount * 2, k, p, height + 1)
    return from_old + from_yang


k, p = map(int, input().split())
answer = count_ents(2, k, p, 0)
print(answer)