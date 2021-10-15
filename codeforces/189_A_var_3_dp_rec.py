import sys


def get_max_pieces(rope_size, a, b, c):
    if rope_size < 0:
        return -1
    if rope_size == 0:
        return 0
    if_last_a = get_max_pieces(rope_size - a, a, b, c)
    if_last_b = get_max_pieces(rope_size - b, a, b, c)
    if_last_c = get_max_pieces(rope_size - c, a, b, c)
    best_variant = max(if_last_a, if_last_b, if_last_c)
    return best_variant + 1 if best_variant >= 0 else -1


sys.setrecursionlimit(40001)

n, a, b, c = map(int, input().strip().split())
print(get_max_pieces(n, a, b, c))