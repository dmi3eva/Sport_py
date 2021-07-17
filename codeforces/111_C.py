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


def my_solution(a):
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


def triple_is_bad(a0, a1, a2):
    increasing = a0 >= a1 >= a2
    decreasing = a0 <= a1 <= a2
    return increasing or decreasing


def four_is_bad(segment):
    first = triple_is_bad(segment[0], segment[1], segment[3])
    second = triple_is_bad(segment[0], segment[2], segment[3])
    third = triple_is_bad(segment[1], segment[2], segment[3])
    return first or second or third

def editorial_solution(a):
    amount = 0
    for ind, number in enumerate(a):
        amount += 1
        if ind < len(a) - 1:
            amount += 1
        if ind < len(a) - 2 and not triple_is_bad(a[ind], a[ind + 1], a[ind + 2]):
            amount += 1
        else:
            continue
        if ind < len(a) - 3 and not four_is_bad(a[ind : ind + 4]):
            amount += 1
    return amount



t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    # answer = my_solution(a)
    answer = editorial_solution(a)
    print(answer)