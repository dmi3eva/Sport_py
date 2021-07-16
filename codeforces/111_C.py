def extract_identical(numbers):
    coordinates = {}
    identicals = []
    for _ind, _num in enumerate(numbers):
        if _num in coordinates.keys():
            identicals.append((coordinates[_num][-1], _ind))
        coordinates[_num] = coordinates.get(_num, []) + [_ind]
    return identicals


def solve(a):
    identicals = extract_identical(a)
    subarray_amount = 0
    for _pair in identicals:
        subarray_amount += 0



t = int(input())
for _ in range(t):
    n = int(input())
    a = map(int, input().strip().split())
    answer = solve(a)
    print(answer)