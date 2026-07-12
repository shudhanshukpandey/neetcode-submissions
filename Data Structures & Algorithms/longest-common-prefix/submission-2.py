class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        s=strs[0]
        for j in range(len(min(strs))):
            for i in range(1,len(strs)):
                if s[j]!=strs[i][j]:
                    return ans
            ans+=s[j]
        return ans