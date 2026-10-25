class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1st
        # return_data = []
        # len_nums = len(nums)

        # for i in range(len_nums):
        #     product = 1
        #     for j in range(len_nums):

        #         if i==j:
        #             continue
        #         product *= nums[j]
        #     return_data.append(product)
        # return return_data

        # 2nd
        len_nums = len(nums)
        prefix = [1]*len_nums
        suffix = [1]*len_nums

        for i in range(1,len_nums):
            prefix[i]=prefix[i-1]*nums[i-1]

        # print(prefix)

        for j in range(len_nums-2, -1, -1):

            suffix[j] = suffix[j+1]*nums[j+1]
        
        # print(suffix)

        return [prefix[i]*suffix[i] for i in range(len_nums) ]


        