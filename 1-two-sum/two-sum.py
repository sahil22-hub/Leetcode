class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_map = {}

        for i,value in enumerate(nums):
            num = target - value
            if num in h_map:
                return [h_map[num],i]
            else:
                h_map[value] = i
            

