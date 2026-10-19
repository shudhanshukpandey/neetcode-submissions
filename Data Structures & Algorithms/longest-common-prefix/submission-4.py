class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # Edge case: if the list is empty, return an empty string
        if not strs:
            return ""
            
        # Use the first word as a reference
        for indx, value in enumerate(strs[0]):
            # Compare this character with the same index in all other words
            for values in strs[1:]:
                # If another word is too short OR its character doesn't match
                if indx >= len(values) or values[indx] != value:
                    # Immediately return everything matched up to this point
                    return strs[0][:indx]
                    
        return strs[0]
