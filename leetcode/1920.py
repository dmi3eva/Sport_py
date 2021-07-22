from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[_v] for _v in nums]

s = Solution()
print(s.buildArray([0,2,1,5,3,4]))