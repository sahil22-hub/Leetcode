class Solution:
    def convert(self, s: str, numRows: int) -> str:
        matrix = [[] for _ in range(numRows)]
        i,j =0,0
        temp = s
        result = ""
        if numRows == 1:
            return s
        while temp:
            while i < numRows and temp:
                matrix[i].append(temp[0])
                temp = temp[1:]
                i += 1
            i -= 1
            while i-1 >= 0 and temp:
                i -= 1
                matrix[i].append(temp[0])
                temp = temp[1:]
            i += 1
        print(matrix)
        for x in matrix:
            k = "".join(x)
            result = result + k
        return result
