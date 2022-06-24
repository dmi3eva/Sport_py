import sys
from typing import *


sys.setrecursionlimit(1000)


def count_ents(start_amount: int, k: int, p: int) -> int:
    if start_amount % p == k:
        return 1
    if start_amount > k:
        return 0
    from_old = count_ents(start_amount + 1, k, p)
    from_yang = count_ents(start_amount * 2, k, p)
    return (from_old + from_yang) % p

# # Восходящая
# dp[2] = 1
# for i in range(k + 1):
#     dp[i * 2] =
#
# # Нисходящая


k, p = map(int, input().split())
answer = count_ents(2, k, p, 0)
print(answer)