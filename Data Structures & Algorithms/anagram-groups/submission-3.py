class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram = dict()

        for input_data in strs:
        #     # print(anagram)
        #     str_len = len(input_data)
        #     if not anagram.get(str_len):
        #         anagram[str_len] = [input_data]
        #         continue
        #     elif anagram.get(str_len) and sorted(input_data)==sorted(anagram[str_len][0]):
        #         anagram[len(input_data)].extend([input_data])
        #     else:
        #         anagram[f'nona_{str_len}'] = anagram.get(f'nona_{str_len}', []) + [input_data]
        # # print(list(anagram.values()))
        # print(anagram)
        # return list(anagram.values())

            sorted_str = "".join(sorted(input_data))
            if not anagram.get(sorted_str):
                anagram[sorted_str] = [input_data]
                continue
            elif anagram.get(sorted_str) and sorted(input_data)==sorted(anagram[sorted_str][0]):
                anagram[sorted_str].extend([input_data])
            
            else:
                anagram[f'nona_{sorted_str}'] = anagram.get(f'nona_{sorted_str}', []) + [input_data]
        # print(list(anagram.values()))
        # print(anagram)
        return list(anagram.values())
            
            
