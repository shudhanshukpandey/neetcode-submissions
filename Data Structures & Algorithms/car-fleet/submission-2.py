class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        zip_data = sorted(zip(position,speed), reverse=True)

        for pos, speed in zip_data:

            target_time = (target-pos)/speed

            if stack and stack[-1]>=target_time:
                continue
            stack.append(target_time)
        
        return len(stack)



        