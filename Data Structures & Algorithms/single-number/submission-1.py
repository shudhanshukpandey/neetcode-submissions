class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for element in nums:
            ans ^= element

        return ans

        