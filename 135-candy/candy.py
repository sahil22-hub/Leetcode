class Solution:
    def candy(self, ratings: List[int]) -> int:
        l = len(ratings)
        candies = [1]*l
        # Left to right pass: handle increasing sequences
        for i in range(1, l):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        
        print(f"After left-to-right: {candies}")
        
        # Right to left pass: handle decreasing sequences
        for i in range(l-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                # Take the maximum between current value and right neighbor + 1
                candies[i] = max(candies[i], candies[i+1] + 1)
        return sum(candies)
            