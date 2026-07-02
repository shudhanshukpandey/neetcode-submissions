class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # existing = dict()

        # for element in nums:
        #     existing[element] = existing.get(element,0)+1

        #     if existing[element]>1:
        #         return True
        # return False

        existing = set()

        for element in nums:
            if element in existing:
                return True
            existing.add(element)
        return False
        