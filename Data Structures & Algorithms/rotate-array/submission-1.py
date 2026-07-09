class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)

        temp = None
        i = 0
        while i < k:

            
            nums.insert(0,nums.pop())
            i+=1

            

            # print(nums)
        return nums


            
        