class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l = len(nums)
        start_index = 0
        end_index = 0
        output = []
        for i in range(l):
            if i == l-1:
                if start_index == end_index:
                    output.append(str(nums[i]))
                else:
                    output.append(f"{nums[start_index]}->{nums[end_index]}")
            elif nums[i+1] == nums[i]+1:
                end_index += 1
            else:
                if start_index == end_index:
                    output.append(str(nums[i]))
                    start_index = end_index + 1
                    end_index = end_index + 1
                else:
                    output.append(f"{nums[start_index]}->{nums[end_index]}")
                    start_index = end_index + 1
                    end_index = end_index + 1
        print(output)
        return output

        