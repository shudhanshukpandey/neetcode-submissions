class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def is_digit(val:str):
            try:
                int(val)
                return True
            except ValueError:
                return False
        stack = []

        for i in tokens:
            print(stack)

            if is_digit(i):
                stack.append(int(i))
            else:
                if i == "+":
                    top_b = stack.pop()
                    top_a = stack.pop()
                    stack.append(top_a+top_b)
                elif i == "-":
                    top_b = stack.pop()
                    top_a = stack.pop()
                    stack.append(top_a-top_b)
                elif i=="*":
                    top_b = stack.pop()
                    top_a = stack.pop()
                    stack.append(top_a*top_b)
                elif i == "/":
                    top_b = stack.pop()
                    top_a = stack.pop()
                    stack.append(int(top_a/top_b))
        
        return stack[-1]


        