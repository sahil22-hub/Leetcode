# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class Solution:
    def threeSum(self,nums):
        nums.sort()  # Sort the array
        result = []
        n = len(nums)

        for i in range(n - 2):  # Loop through the array
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates for nums[i]
                continue

            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1  # Move left pointer to increase the sum
                elif total > 0:
                    right -= 1  # Move right pointer to decrease the sum
                else:
                    result.append([nums[i], nums[left], nums[right]])  # Found a valid triplet

                    # Skip duplicates for nums[left] and nums[right]
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers
                    left += 1
                    right -= 1

        return result
    # def threeSum(self, nums):
    #     l = len(nums)
    #     #handle edge cases
    #     if l < 3:
    #         return []
    #     nums.sort()
    #     print(nums)
    #     pointer = 0
    #     output = []
    #     for i in range(l-1):
    #         # if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates for nums[i]
    #         #     continue

    #         pointer = i
    #         first = i+1
    #         second = l-1
    #         while first < second:
    #             if nums[first] + nums[second] == -nums[pointer]:
    #                 if not [nums[pointer], nums[first], nums[second]] in output:
    #                     output.append([nums[pointer], nums[first], nums[second]])
    #                 print([nums[pointer], nums[first], nums[second]])
    #                 print(i)
    #                 while first < second and nums[first] == nums[first+1] :
    #                     first += 1
    #                 while first < second and nums[second] == nums[second-1]:
    #                     second -= 1
    #                 first += 1
    #                 second -= 1
                        
    #             # decrease the second if we require value smaller
    #             elif nums[first] + nums[second] > -nums[pointer]:
    #                 first += 1
    #              # increase the first if we require value bigger
    #             else:
    #                 second -= 1
    #     return output

