class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_num = set()
        j = 0
        for i, value in enumerate(nums):
            if value not in unique_num:
                unique_num.add(value)
                nums[j] = value
                j += 1
        return j
        