from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        
        # Sort cars based on position in descending order (closest to target first)
        zip_data = sorted(zip(position, speed), reverse=True)
        
        for pos, spd in zip_data:
            # Use floating-point division for accurate arrival times
            target_time = (target - pos) / spd
            
            # If the current car arrives sooner or at the same time as the fleet ahead,
            # it will catch up and merge into that fleet. We skip adding it.
            if stack and stack[-1] >= target_time:
                continue
                
            # If it takes longer, it becomes the bottleneck/leader of a new fleet.
            stack.append(target_time)
            
        return len(stack)
