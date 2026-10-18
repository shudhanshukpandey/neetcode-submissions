class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        feq = {}
        for i in range(len(s)):
            feq[s[i]] = feq.get(s[i], 0) + 1
            feq[t[i]] = feq.get(t[i], 0)-1
        # print(feq)
        return not any(feq.values())
        