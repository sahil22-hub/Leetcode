class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sorted_x = sorted(citations, key = lambda x : -x)
        l = len(sorted_x)
        h_value = 0
        for i in range(1,l+1):
            if sorted_x[i-1] >= i:
                h_value = i

        return h_value