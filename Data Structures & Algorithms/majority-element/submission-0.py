class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        major_element =nums[0]
        count =1

        for i in nums[1:]:
            if i == major_element:
                count+=1
            else:
                count-=1

            if count ==0:
                major_element = i
                count+=1
        return major_element
        