class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            # Loop runs only when a collision is possible:
            # Top of stack moves right (+) and current asteroid moves left (-)
            while stack and ast < 0 < stack[-1]:
                # Case 1: Both asteroids are the same size. Both explode.
                if stack[-1] == -ast:
                    stack.pop()
                    break
                # Case 2: Top of stack is smaller. It explodes, current keeps moving.
                elif stack[-1] < -ast:
                    stack.pop()
                    continue
                # Case 3: Top of stack is larger. Current asteroid explodes.
                else:
                    break
            else:
                # Executes only if the while loop finishes normally without a 'break'
                # (Meaning the current asteroid survived all collisions or didn't collide)
                stack.append(ast)
                
        return stack