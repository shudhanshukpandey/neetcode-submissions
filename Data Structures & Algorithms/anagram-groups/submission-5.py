class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        return_data = {}

        for word in strs:

            key = "".join(sorted(word))

            return_data[key] = return_data.get(key,[])+[word]

        return list(return_data.values())
        