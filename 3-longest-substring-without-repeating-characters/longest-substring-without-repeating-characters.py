class Solution(object):
    def lengthOfLongestSubstring(self, s):
        substring = ""
        left = 0
        max_length = 0

        for right in range(len(s)):
            if s[right] in substring:
                print(s[right],substring)
                substring = substring[substring.find(s[right])+1:]
                print(s.find(s[right]))
            
            substring  += s[right]
            print(substring)
            max_length = max(max_length, len(substring))


        return max_length
                
