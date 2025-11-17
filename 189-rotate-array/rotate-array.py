class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k == 0:
            return
        
        n = len(nums)
        
        result = [0]*n
        for i in range(n):
            result[(i + k) % n] = nums[i]
        
        # Copy back to original array
        for i in range(n):
            nums[i] = result[i]


        