class Solution:
    def calPoints(self, operations: List[str]) -> int:
        def is_integer(val:str):
            try:
                int(val)
                return  True
            except ValueError:
                return False
        stack = []

        for i in operations:
            # print(stack)
            if is_integer(i):
                stack.append(int(i))
                # print(stack)
            elif i=='+':
                stack.append(stack[-1]+stack[-2])
            elif i=="C":
                stack.pop()
            elif i=="D":
                stack.append(stack[-1]*2)
        # print(stack)
            
        return sum(stack)
        