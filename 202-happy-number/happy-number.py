class Solution:
    def isHappy(self, n: int) -> bool:   
        count = len(str(n))
        track = []
        while n != 1 and n not in track:
            track.append(n)
            n = sum(int(num)**2 for num in str(n))
        return n == 1
            


        
        