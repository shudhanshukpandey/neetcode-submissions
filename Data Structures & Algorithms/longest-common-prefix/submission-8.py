class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        
        return_data = ""
        if not strs:
            return return_data
        # 1st
        # for i in zip(*strs):

        #     if len(set(i))==1:
        #         return_data+=i[0]
        #     else:
        #         break
        # return return_data
    # 2nd

        for indx, char in enumerate(strs[0]):

            for word in strs[1:]:

                if indx>=len(word) or word[indx]!=char:
                    return strs[0][:indx]
        return strs[0]

            
        