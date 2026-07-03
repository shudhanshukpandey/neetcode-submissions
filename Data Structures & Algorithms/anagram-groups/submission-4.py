class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        return_val = defaultdict(list)

        for item in strs:
            count = [0]*26

            for char in item:
                count[ord(char)-ord('a')]+=1
            
            return_val[tuple(count)].append(item)

        return list(return_val.values())
        