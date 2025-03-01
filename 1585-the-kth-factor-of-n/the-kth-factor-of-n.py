class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        if n == 0:
            return -1
        lst = [] #store factorial
        temp = 0
        for x in range(1,int(n**0.5)+1):
            if n % x == 0:
                lst.append(x)
                if x != n // x:
                    lst.append(n//x)
        lst.sort()
        print(lst)
        return lst[k-1] if len(lst) >= k else -1
        