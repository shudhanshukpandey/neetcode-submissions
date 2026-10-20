class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        return_data = {}

        # 1st
        # for word in strs:

        #     key = "".join(sorted(word.lower()))

        #     return_data[key] = return_data.get(key,[])+[word]

        # return list(return_data.values())

        # 2nd

        for word in strs:

            key = [0]*26

            for char in word.lower():

                key[ord(char)-ord('a')]+=1

            return_data[tuple(key)] = return_data.get(tuple(key), []) + [word]
        return list(return_data.values())
        