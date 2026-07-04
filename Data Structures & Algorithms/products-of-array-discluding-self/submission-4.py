class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        len_nums = len(nums)
        prefix = [1]*len_nums
        suffix = [1]*len_nums

        for i in range(1,len_nums):
            prefix[i] = prefix[i-1]*nums[i-1]
        
        # print(prefix)

        for j in range(len_nums-2,-1,-1):
            suffix[j] = suffix[j+1]*nums[j+1]
        
        # print(suffix)

        response = [0]*len_nums
        for k in range(len_nums):

            response[k] = prefix[k]*suffix[k]
        
        return response
        