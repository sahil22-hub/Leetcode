class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #count the number of occurance
        count = 0
        for value in nums:
            if count < 2 or value != nums[count-2]:
               nums[count] = value
               count += 1
        print(count)        
        return count
                