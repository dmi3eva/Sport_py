from typing import *


def is_list_contains(source: List[int], target: int) -> bool:
    l = 0
    r = len(source) - 1
    while l < r:
        m = (l + r) // 2
        if source[m] < target:
            l = m + 1
        else:
            r = m
    return source[r] == target


n, k = map(int, input().strip().split())
source = list(map(int, input().strip().split()))
values_for_search = list(map(int, input().strip().split()))

for target in values_for_search:
    if is_list_contains(source, target):
        print("YES")
    else:
        print("NO")
