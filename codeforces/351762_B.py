n = int(input())
all_students = list(map(int, input().strip().split()))
max_value = max(all_students)
min_value = min(all_students)
good_students = [_v for _v in all_students if _v != max_value and _v != min_value]
print(max(len(good_students), 0))