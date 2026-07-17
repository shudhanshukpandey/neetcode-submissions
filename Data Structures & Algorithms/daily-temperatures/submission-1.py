class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        len_temps = len(temperatures)
        stack = []
        result = [0]*len_temps

        for i in range(len_temps):
            while stack and stack[-1][0]<temperatures[i]:
                last_val, last_indx  = stack.pop()
                result[last_indx] = i- last_indx
            
            stack.append((temperatures[i], i))
        return result

        