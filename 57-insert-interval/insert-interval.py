class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        s = sorted(intervals)
        l = len(s)
        output = []
        for i in range(l):
            if(i == l-1):
                output.append(s[i])
                break
            if s[i][-1] in range(s[i+1][0],s[i+1][-1]+1) or s[i+1][-1] in range(s[i][0],s[i][-1]+1):
                minimum,maximum = min(s[i]+s[i+1]), max(s[i]+s[i+1])
                s[i+1] = [minimum,maximum]
            else:
                print("from else",i)
                print(output)
                output.append(s[i])
        print(output)
        return output
        # output = []
        # l = len(intervals)
        # for i in range(l):
        #     if newInterval[0] in range(intervals[i][0],intervals[i][-1]+1) or newInterval[-1] in range(intervals[i][0],intervals[i][-1]+1):
        #         minimum,maximum = min(intervals[i]+ newInterval), max(intervals[i]+newInterval)
        #          = [minimum,maximum]