class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        keyboard = {
            2:['a', 'b', 'c'],
            3:['d', 'e', 'f'],
            4:['g', 'h', 'i'],
            5:['j', 'k', 'l'],
            6:['m', 'n', 'o'],
            7:['p', 'q', 'r', 's'],
            8:['t', 'u', 'v'],
            9:['w', 'x', 'y', 'z']
        }

        # selected_chars = []
        # for i in digits:
        #     selected_chars.append(keyboard.get(int(i)))

        # print(selected_chars)
        from itertools import product
        return_data = [''.join(p) for p in product(*[keyboard.get(int(i)) for i in digits]) if p]

        # print(return_data)

        return return_data
        