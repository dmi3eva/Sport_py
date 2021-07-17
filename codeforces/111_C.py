def extract_identical(numbers):
    coordinates = {}
    identicals = []
    for _ind, _num in enumerate(numbers):
        if _num in coordinates.keys():
            identicals.append((coordinates[_num][-1], _ind))
        coordinates[_num] = coordinates.get(_num, []) + [_ind]
    return identicals


def extract_segments(numbers):
    segments = []
    for first_ind, _number in enumerate(numbers):
        end_ind = len(numbers)
        second_ind = first_ind + 1
        segment = None
        while end_ind > second_ind:
            third_ind = second_ind + 1
            while third_ind < end_ind:
                increasing = numbers[second_ind] >= numbers[first_ind] and numbers[third_ind] >= numbers[second_ind]
                decreasing = numbers[second_ind] <= numbers[first_ind] and numbers[third_ind] <= numbers[second_ind]
                if increasing or decreasing:
                    segment = (first_ind, third_ind)
                    end_ind = third_ind
                third_ind += 1
            second_ind += 1
        if segment:
            segments.append(segment)
    return segments


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