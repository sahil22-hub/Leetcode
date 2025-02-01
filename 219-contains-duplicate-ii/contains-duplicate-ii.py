class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h_map = {}
        for i, value in enumerate(nums):
            if value in h_map.keys() and abs(i - h_map[value]) <= k:
                return True
            else:
                h_map[value]= i
        return False
                