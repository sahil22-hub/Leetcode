class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        if n == 0:
            return -1
        lst = []
        temp = 0
        for x in range(1,n+1):
            if n % x == 0:
                temp += 1
                lst.append(x)
            if temp == k:
                print(lst)
                return lst[k-1]
        return -1



        