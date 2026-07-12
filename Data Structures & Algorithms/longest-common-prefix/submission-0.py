class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = ""
        # zip(*strs) groups characters from each string by their column index
        for chars in zip(*strs):
            # If all characters in the column are identical, the set length is 1
            if len(set(chars)) == 1:
                result += chars[0]
            else:
                break
        return result
