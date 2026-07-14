class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = {}

        for indx, val in enumerate(nums):
            if val in mp and abs(mp[val]-indx)<= k:
                return  True
            
            mp[val] = indx

        return False
        