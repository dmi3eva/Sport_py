def extract_identical(numbers):
    coordinates = {}
    identicals = []
    for _ind, _num in enumerate(numbers):
        if _num in coordinates.keys():
            identicals.append((coordinates[_num][-1], _ind))
            print(_num)
            print(identicals)
        coordinates[_num] = coordinates.get(_num, []) + [_ind]
    print(identicals)
    return identicals



def solve(a):
    identical_numbers = extract_identical(a)


t = int(input())
for _ in range(t):
    n = int(input())
    a = map(int, input().strip().split())
    answer = solve(a)
    print(extract_identical(a))