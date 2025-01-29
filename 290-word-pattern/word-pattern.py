class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        temp = s.split(" ")
        l = len(pattern)
        value = {}
        if l != len(temp):
            return False
        for i in range(l):
            if pattern[i] in value.keys():
                print("from keys;",value)
                if value[pattern[i]] != temp[i]:
                    return False
            else:
                print(value)
                if temp[i] in value.values():
                    return False
                value[pattern[i]] = temp[i]
        return True