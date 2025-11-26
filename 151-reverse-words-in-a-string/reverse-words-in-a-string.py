class Solution:
    def reverseWords(self, s: str) -> str:
        temp = s.split()
        print(temp)
        temp = temp[::-1]
        return " ".join(temp)

        