from typing import *




def quick_sort(numbers: List[int]) -> List[int]:
    if len(numbers) <= 1:
        return numbers
    pivot_ind = len(numbers) // 2
    pivot_value = numbers[pivot_ind]
    less = [_n for _n in numbers if _n < pivot_value]
    greater = [_n for _n in numbers if _n > pivot_value]
    less = quick_sort(less)
    greater = quick_sort(greater)
    return less + [pivot_value] + greater


if __name__ == "__main__":
    n = int(input())
    values = list(map(int, input().split()))
    sorted_values = quick_sort(values)
    for _value in sorted_values:
        print(_value, end=' ')