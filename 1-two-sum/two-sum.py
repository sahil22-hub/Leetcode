class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store_map = {}

        for i, num in enumerate(nums):
            n2 = target - num
            if n2 in store_map:
                return [i,store_map[n2]]
            store_map[num] = i
            

        