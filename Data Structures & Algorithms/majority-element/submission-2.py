class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major_ele = nums[0]
        count = 1

        for ele in nums[1:]:
            # print(count, major_ele)

            if ele==major_ele:
                count+=1
            else:
                count-=1
            
            if count==0:
                major_ele = ele
                count=1
        return major_ele
        