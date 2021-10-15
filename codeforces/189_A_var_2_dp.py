n, a, b, c = map(int, input().strip().split())
a, b, c = sorted([a, b, c])

pieces_nums = [0] + [-1 for _ in range(a - 1)]

for rope_size in range(a, n + 1):
    last_is_a = pieces_nums[rope_size - a] + 1 if rope_size >= a and pieces_nums[rope_size - a] != -1 else -1
    last_is_b = pieces_nums[rope_size - b] + 1 if rope_size >= b and pieces_nums[rope_size - b] != -1 else -1
    last_is_c = pieces_nums[rope_size - c] + 1 if rope_size >= c and pieces_nums[rope_size - c] != -1 else -1
    max_pieces = max(last_is_a, last_is_b, last_is_c)
    pieces_nums.append(max_pieces)

print(pieces_nums[n])