class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = prices[0]
        max_profit = 0
        current_profit = 0
        for i in prices:
            # print(i, min_price,current_profit, max_profit)
            
            min_price = min(min_price, i)
            current_profit = max(current_profit, i-min_price)
            if current_profit:
                # print("casper")
                max_profit+=current_profit
                current_profit = 0
                min_price = i
        # print(i, min_price, current_profit,max_profit)
        return max_profit