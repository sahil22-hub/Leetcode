class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        l = len(sorted_nums)
        counts = []
        counter = 0
        if l == 1:
            counts.append(0)
        else:
            for i in range(l-1):
                if sorted_nums[i+1] == sorted_nums[i] + 1:
                    counter += 1
                    print("from if: ",sorted_nums[i+1],counter)
                    counts.append(counter)
                elif sorted_nums[i] == sorted_nums[i+1]:
                    print("elif :: ", sorted_nums[i+1],counter)
                    continue
                else:
                    print("from else: ",sorted_nums[i+1],counter)
                    counts.append(counter)
                    counter = 0
        if l >= 1 and counter == 0:
            counts.append(0)
        print(counts)
        return max(counts)+1 if counts else 0
            