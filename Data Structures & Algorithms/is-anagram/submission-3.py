class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        checker = dict()
        for element in s:
            checker[element] = checker.get(element,0)+1

        for element in t:
            if element in checker:
                checker[element]= checker.get(element,0)-1
                continue
            checker[element] = checker.get(element,0)+1
            

        print(checker)
        anagram = any(i for i in checker.values())
        print(anagram)
        return not anagram
        
        