from collections import defaultdict
class Solution:
    def findAnagrams(self,s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []

        p_count = defaultdict(int)
        s_count = defaultdict(int)

        for char in p:
            p_count[char] += 1

        for i in range(len(p)):
            s_count[s[i]] += 1

        print(p_count)
        print(s_count)
        result = []

        if s_count == p_count:
            result.append(0)

        for i in range(0,len(s)-len(p)):
            left_char = s[i]
            s_count[left_char] -= 1
            if s_count[left_char] == 0:
                del s_count[left_char]
            right_char = s[i+len(p)]
            s_count[right_char] += 1

            if s_count == p_count:
                result.append(i+1)


        # for i in range(len(p), len(s)):
        #     left_char = s[i - len(p)]
        #     s_count[left_char] -= 1
        #     if s_count[left_char] == 0:
        #         del s_count[left_char]

        #     right_char = s[i]
        #     s_count[right_char] += 1

        #     if s_count == p_count:
        #         result.append(i - len(p) + 1)

        return result


            
            