class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        l1 = len(word1)
        l2 = len(word2)
        first, second = 0, 0
        
        # Iterate through both strings and add characters alternately
        while first < l1 or second < l2:
            if first < l1:
                result += word1[first]
                first += 1
            if second < l2:
                result += word2[second]
                second += 1
        
        return result