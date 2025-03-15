class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        if not grid:
            return 0
        rows, columns = len(grid),len(grid[0])

        def dfs(rw,cl):
            if rw < 0 or rw >= rows or cl < 0 or cl >= columns or grid[rw][cl] == "0":
                return
            
            #mark the visited node as 0
            grid[rw][cl] = "0"

            #traverse through horizontal and vertical until zero is found than stop as the            island is ended for that particular direction
            dfs(rw-1,cl)# up
            dfs(rw+1,cl)# down
            dfs(rw,cl-1) #left
            dfs(rw,cl+1) #right

        # Iterate through the grid
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == '1':
                    # Start DFS to mark the entire island
                    dfs(r, c)
                    # Increment island count
                    count += 1

        return count
