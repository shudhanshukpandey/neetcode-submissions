class Solution:
    def trap(self, height: List[int]) -> int:
        
        len_height = len(height)

        left_max = [0]*len_height
        right_max = [0]*len_height

        res = 0

        left_max[0] = height[0]
        for i in range(1,len_height):
            left_max[i] = max(left_max[i-1], height[i])

        right_max[len_height-1] = height[len_height-1]
        for j in range(len_height - 2, -1, -1):
            right_max[j] = max(right_max[j+1],height[j])

        for i in range(1, len_height- 1):
            min_of_2 = min(left_max[i], right_max[i])
            res += min_of_2 - height[i]

        return res


        
        