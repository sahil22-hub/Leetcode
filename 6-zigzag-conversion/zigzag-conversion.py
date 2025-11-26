class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        #create rows
        rows = ['']*numRows
        current_row = 0
        down = False

        for char in s:
            rows[current_row] += char

            if current_row == 0 or current_row == numRows - 1:
                down = not down

            # Move to next row
            current_row += 1 if down else -1
        print(rows)

        return ''.join(rows)

        