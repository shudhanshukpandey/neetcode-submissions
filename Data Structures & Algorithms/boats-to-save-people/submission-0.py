class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        mp = dict()
        people.sort()
        
        i,j = 0, len(people)-1
        counter=0
        while i<j:

            if people[i]+people[j]<=limit:
                counter+=1
                i+=1
                j-=1
            else:
                counter+=1
                j-=1
            if i==j:
                counter+=1
            
        return counter


        