class Solution:
    def hammingWeight(self, n: int) -> int:

        counter = 0
        
    
        for i in bin(n):
           
            if i =='1':
                counter+=1
        return counter
        