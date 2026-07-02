class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        # checker = dict()
        # for element in s:
        #     checker[element] = checker.get(element,0)+1

        # for element in t:
        #     if element in checker:
        #         checker[element]= checker.get(element,0)-1
        #         continue
        #     checker[element] = checker.get(element,0)+1
            

        # anagram = any(i for i in checker.values())
        # return not anagram

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
        
        