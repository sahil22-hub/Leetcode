class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        pointer1 = 0
        pointer2 = 0
        temp = []
        
        while pointer1 < m and pointer2 < n:
            if nums1[pointer1] <= nums2[pointer2]:
                temp.append(nums1[pointer1])
                pointer1 += 1
            else:
                temp.append(nums2[pointer2])
                pointer2 += 1
        
        # Add remaining elements from nums1
        while pointer1 < m:
            temp.append(nums1[pointer1])
            pointer1 += 1
        
        # Add remaining elements from nums2
        while pointer2 < n:
            temp.append(nums2[pointer2])
            pointer2 += 1
        
        # Copy temp back to nums1 (modify in-place)
        for i in range(len(temp)):
            nums1[i] = temp[i]