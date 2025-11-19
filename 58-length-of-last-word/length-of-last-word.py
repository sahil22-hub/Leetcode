class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst = s.split(" ")
        words = [x for x in lst if x!=""]
        return len(words[-1])
        