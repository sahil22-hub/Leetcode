class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = []
        output = []
        if len(points) < k:
            return []
        for x,y in points:
            dis.append([sqrt(pow(x,2)+pow(y,2)),x,y])
        print(dis)
        dis.sort(key = lambda x: x[0])
        print(dis)
        for i in range(k):
            output.append(dis[i][1:])
        return output 
            

        