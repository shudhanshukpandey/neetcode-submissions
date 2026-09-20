class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        nums_sum = sum(nums)
        total_sum = len(nums)*(len(nums)+1)//2

        return 0 if nums_sum == total_sum else total_sum-nums_sum

        