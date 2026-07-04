class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero = False
        zindx = []
        product = 1

        len_nums = len(nums)
        return_data = [0]*len_nums

        for indx, value in enumerate(nums):
            if value==0:
                zero = True
                zindx.append(indx)
                continue
            product *= value
        
        if zero:
            if len(zindx)>1:
                return [0]*len_nums
            return_data = [product if i in zindx else 0 for i in range(len_nums)]
            return return_data
        
        for i in range(len_nums):
            return_data[i] = product//nums[i]

        return return_data 


        