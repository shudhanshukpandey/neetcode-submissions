class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        existing = dict()

        for element in nums:
            existing[element] = existing.get(element,0)+1

            if existing[element]>1:
                return True
        return False
        