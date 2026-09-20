class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        all_nums_xor = 0
        for i in range(n + 1):
            all_nums_xor ^= i
        
        input_list_xor = 0
        for num in nums:
            input_list_xor ^= num
        
        return all_nums_xor ^ input_list_xor