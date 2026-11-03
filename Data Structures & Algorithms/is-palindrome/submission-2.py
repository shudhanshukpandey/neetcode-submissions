class Solution:
    def isPalindrome(self, s: str) -> bool:

        final_str = "".join(i if i.isalnum() else "" for i in s.lower())

        # print(final_str)
        # 1st
        # i ,j = 0, len(final_str)-1

        # while i<j:
        #     if not final_str[i]==final_str[j]:
        #         return False
        #     i+=1
        #     j-=1
        # return True

        return final_str == final_str[::-1]
        