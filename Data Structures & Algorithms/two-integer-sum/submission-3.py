class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # nums.sort()

        # i, j = 0, len(nums)-1

        # while i<j:
        #     if nums[i]+nums[j]==target:
        #         return [i,j]
        #     elif nums[i]+nums[j]<target:
        #         i+=1
        #     else:
        #         j-=1

        for indx, val in enumerate(nums):

            diff = target-val

            if diff in nums and nums.index(diff)!=indx:
                # print(target,diff, indx, nums.index(diff))
                return sorted([indx,nums.index(diff)])

                # ineffieient use solution 2