class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j=0,0
        encountered = set()
        max_len = 0
        while j<len(s):
            if s[j] in encountered:
                encountered.remove(s[i])
                i+=1
                continue
            encountered.add(s[j])
            j+=1
            max_len = max(max_len, len(encountered))
        return max_len

        