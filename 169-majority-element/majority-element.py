class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for value in nums:
            if value not in count:
                count[value] = 1
            else:
                count[value] += 1
        max_count = max(count.values())
        return [key for key, value in count.items() if value == max_count][0]
        