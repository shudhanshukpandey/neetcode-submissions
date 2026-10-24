class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = curSum = 0
        prefixSums = { 0 : 1 }

        for num in nums:
            
            curSum += num
            diff = curSum - k
            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)

        return res

"""
very inefficient:-


def subarraySum(nums, k) -> int:

    i, j =0,0
    counter = 0
    while i < len(nums):

        print(i,j , counter, nums[i:j])

        if sum(nums[i:j+1])==k:
            counter+=1
        j+=1
        if j>=len(nums):
            i+=1
            j=i
    
    return counter

print(subarraySum([4,4,4,4,4], 8))


⚠️ Performance Alert

While your logic works, using sum(nums[i:j+1]) inside a nested manual loop results in a O(N³) time complexity. Slicing nums[i:j] also creates extra lists in memory.

"""