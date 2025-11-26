class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        common_list = strs[0]
        n = len(strs)
        for i in range(1,n):
            length = len(strs[i])
            j = 0
            while j < length and j < len(common_list):
                if strs[i][j] != common_list[j]:
                   break
                j += 1
            common_list = common_list[:j]

        
        return common_list

        