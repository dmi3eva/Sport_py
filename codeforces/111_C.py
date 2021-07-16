def extract_identical(numbers):
    coordinates = {}
    identicals = []
    for _ind, _num in enumerate(numbers):
        if _num in coordinates.keys():
            identicals.append((coordinates[_num][-1], _ind))
        coordinates[_num] = coordinates.get(_num, []) + [_ind]
    return identicals


def extract_segments(numbers):
    return extract_identical(numbers)


def solve(a):
    identicals = extract_segments(a) + [(len(a) - 1, len(a))]
    subarray_amount = 0
    s_ind = 0
    for _pair in identicals:
        if _pair[0] < s_ind:
            continue
        a = _pair[0]
        b = _pair[1]
        a0 = b - s_ind
        n = a - s_ind + 1
        subarray_amount += n * (2 * a0 - n + 1) // 2
        s_ind = a + 1
    return subarray_amount

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    answer = solve(a)
    print(answer)