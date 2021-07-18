from typing import List


class Solution_01: # 100 ms 14.7 mb
    """"
    has a time complexity of O(1) assuming that the concatenation operation takes O(1) time.
    """
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

class Solution_02: # 129 ms 14.3 mb
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return [*nums, *nums]

class AnotherSolution_03: # 132 ms 14.4 mb
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2

# solution = Solution()
solution = Solution_01()
print(solution.getConcatenation([1, 2, 3]))