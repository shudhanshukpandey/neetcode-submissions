class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i =0
        j= len(nums)-1

        loop = 0
        temp = None

        while loop<=j:
            # print(nums)

            if nums[loop]==0:

                nums[i],nums[loop] = nums[loop], nums[i]
                i+=1
                loop+=1
            elif nums[loop]==2:
                nums[j],nums[loop] = nums[loop],nums[j]
                j-=1
            else:
                loop+=1
        
        print(nums)


        