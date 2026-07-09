class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = min(len(word1), len(word2))

        s = []
        i = 0
        while i <min_len:

            s.append(word1[i])
            s.append(word2[i])

            i+=1

        s+=word1[min_len:] + word2[min_len:]

        return "".join(s)
        