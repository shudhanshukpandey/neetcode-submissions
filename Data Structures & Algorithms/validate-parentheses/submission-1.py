class Solution:
    def isValid(self, s: str) -> bool:

        close_map = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        stack = []

        for i in s:
            if i not in close_map:
                stack.append(i)
                continue
            elif i in close_map and stack and stack[-1] == close_map.get(i):
                stack.pop()
            else:
                stack.append(i)
        return False if stack else True
        