# class Solution:
#     def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # current_speed = 1
        # while True:
        #     total_time_consumed = 0
        #     for pile in piles:
        #         total_time_consumed+= math.ceil(pile/current_speed)

        #     if total_time_consumed<=h:
        #         return current_speed
            
        #     current_speed+=1
        # return current_speed

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res


        