class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l = len(p)
        sorted_ = "".join(sorted(p))
        print(sorted_)
        ll = len(s)
        count = 0
        output = []
        while count <= ll-l:
            temp = "".join(sorted(s[count:count+l]))
            if sorted_ == temp:
                output.append(count)
            count += 1
        return output


        
        