class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        seen = set()
        for element in nums:
            if element in seen:
                seen.remove(element)
                continue
            seen.add(element)
        
        return list(seen)[0]
        