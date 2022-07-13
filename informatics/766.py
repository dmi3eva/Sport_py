from typing import *


def partition(numbers: List[int], left: int, right: int) -> List[int]:
    pivot_ind = (left + right) // 2
    pivot_value = numbers[pivot_ind]
    less = left
    greater = right - 1
    while less < greater:
        while numbers[less] < pivot_value:
            less += 1
        while numbers[greater] > pivot_value:
            greater -= 1
        numbers[less], numbers[greater] = numbers[greater], numbers[less]
    return numbers


def quick_sort(numbers: List[int], left: int, right: int) -> List[int]:
    if right - left <= 1:
        return numbers
    pivot_ind = (left + right) // 2
    numbers = partition(numbers, left, right)
    numbers = quick_sort(numbers, left, pivot_ind)
    numbers = quick_sort(numbers, pivot_ind, right)
    return numbers


if __name__ == "__main__":
    n = int(input())
    values = list(map(int, input().split()))
    sorted_values = quick_sort(values, 0, len(values))
    for _value in sorted_values:
        print(_value, end=' ')