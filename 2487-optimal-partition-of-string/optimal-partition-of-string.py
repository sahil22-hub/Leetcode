class Solution:
    def partitionString(self, s: str) -> int:
        l = len(s)
        temp = ""
        sub = []
        if l == 0:
            return 0
        if l == 1:
            return 1
        for i in range(l):
            if s[i] not in temp:
                temp += s[i]
            else:
                sub.append(temp)
                temp = s[i]
        sub.append(temp)
        print(sub)
        return len(sub)

        