class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # 1st
        return_data = ""
        if not strs:
            return return_data
        
        for i in zip(*strs):

            if len(set(i))==1:
                return_data+=i[0]
            else:
                break
        return return_data
            
        