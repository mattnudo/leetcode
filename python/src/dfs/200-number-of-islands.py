from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col):
            # Mark the current cell as '0' to indicate the land is visited
            grid[row][col] = '0'
            #dfs and set 1s to 0 as we traverse the grid
            #create 4 dim search array and traverse adjacent cells
            for dx, dy in [[0,1], [0,-1], [1,0], [-1,0]]:
                delta_x, delta_y = row+dx, col+dy
                if 0 <= delta_x < rows and 0 <= delta_y < cols and grid[delta_x][delta_y] == '1':
                    dfs(delta_x, delta_y)
            #if the element is within bounds and a 1, dfs it
        
        #count # of islands
        islands = 0
        #track size of grid
        rows, cols = len(grid), len(grid[0])
        #traverse rows and cols
        for row in range(rows):
            for col in range(cols):
                if(grid[row][col] == '1'):
                    islands += 1
                    dfs(row, col)
        #when we find a new 1 in the top level search, we increment islands

        return islands
