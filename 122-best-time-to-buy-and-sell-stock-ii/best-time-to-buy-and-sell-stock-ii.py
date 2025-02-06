class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = float('inf')
        maxp = 0
        total = 0
        for x in range(len(prices)):
            if maxp > 0 and prices[x]<prices[x-1]:
                minp = float('inf')
                total += maxp
                maxp = 0
            minp = min(minp,prices[x])
            maxp = max(maxp,prices[x]-minp)
        total += maxp
        return total














        # minvalue = float('inf')
        # profit = 0
        # numbers = len(prices)
        # i = 0 
        # final_profit = 0
        # while i < numbers:
        #     minvalue = min(prices[i],minvalue)
        #     profit = max(profit,prices[i]-minvalue)
        #     if i != numbers-1:
        #         if prices[i] > prices[i+1]:
        #             minvalue = float('inf')
        #             final_profit += profit
        #             profit = 0 
        #     else:
        #         final_profit += profit
        #     i += 1

        # print(profit)
        # return final_profit if final_profit !=0 else profit