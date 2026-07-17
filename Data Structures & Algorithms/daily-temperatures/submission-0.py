class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        len_temps = len(temperatures)
        stack = []
        result = [0]*len_temps
        
        for i in range(len_temps):
            counter = 0
            for j in range(i+1,len_temps):
                # print(i,j, counter, result,temperatures[i],temperatures[j])
                if temperatures[j]>temperatures[i]:
                    counter+=1
                    result[i] = counter
                    break
                else:
                    counter+=1
                    # continue
            # print(counter, j)
        return result

        