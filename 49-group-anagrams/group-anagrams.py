class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dd = {}
        # for word in strs:
        #     temp = "".join(sorted(word))
        #     print(word,temp)
        #     if temp in dd.keys():
        #         dd[temp].append(word)
        #     else:
        #         dd[temp] = [word]
        # return list(dd.values())














        sorted_lst = ["".join(sorted(word)) for word in strs]
        print(sorted_lst)
        l = len(strs)
        temp = {}
        for i in range(l):
            if sorted_lst[i] in temp.keys():
                temp[sorted_lst[i]].append(strs[i])
            else:
                temp[sorted_lst[i]] = [strs[i]]
        print(temp.values())
        return list(temp.values())
        