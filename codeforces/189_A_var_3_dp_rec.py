import sys

def get_max_pieces(rope_size, a, b, c):
    if rope_size < a or rope_size < 0:
        return None
    max_pieces = get_max_pieces(rope_size - a, a, b, c) + 1
    if_last_b = get_max_pieces(rope_size - b, a, b, c) + 1
    if if_last_b:
        max_pieces = max(max_pieces, if_last_b)
    if_last_c = get_max_pieces(rope_size - c, a, b, c) + 1
    if if_last_c:
        max_pieces = max(max_pieces, if_last_c)
    return max_pieces

sys.setrecursionlimit(4001)

n, a, b, c = map(int, input().strip().split())
a, b, c = sorted([a, b, c])

pieces_nums = [0] + [-1 for _ in range(a - 1)]

for rope_size in range(a, n + 1):
    last_is_a = pieces_nums[max(rope_size - a, 0)] + 1 if pieces_nums[max(rope_size - a, 0)] != -1 else -1
    last_is_b = pieces_nums[max(rope_size - b, 0)] + 1 if pieces_nums[max(rope_size - b, 0)] != -1 else -1
    last_is_c = pieces_nums[max(rope_size - c, 0)] + 1 if pieces_nums[max(rope_size - c, 0)] != -1 else -1
    max_pieces = max(last_is_a, last_is_b, last_is_c)
    pieces_nums.append(max_pieces)


print(pieces_nums[n])