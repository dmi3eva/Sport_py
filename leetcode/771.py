class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return len([_s for _s in stones if _s in jewels])

s = Solution()
print(s.numJewelsInStones("aA", "aAAbbbb"))