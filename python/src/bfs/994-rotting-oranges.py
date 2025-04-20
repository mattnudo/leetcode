from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #deltas over time -> BFS, each round of bfs is a minute
        #track dimensions of grid
        rows, columns = len(grid), len(grid[0])
        #use a queue, enqueue rotten fruit, and look at adjacent fresh fruit
        queue = deque()
        #track how many rounds of rotting occur
        minutes=0
        fresh = 0

        #iterate over rows and cols
        for row in range(rows):
            for column in range(columns):
                if(grid[row][column] == 2):
                    queue.append((row, column)) #enqueue rotten fruits
                if(grid[row][column] == 1):
                    fresh += 1 #count up fresh fruits
        
        #while queue and fresh > 0
        while (queue and fresh > 0):
            minutes += 1
            #pop a queue element and iterate
            for _ in range(len(queue)):
                x, y = queue.popleft()
                
                #for 4 directions, look for fresh fruits
                for delta_row, delta_col in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    i, j = x + delta_row, y + delta_col
                  
                    # If the adjacent cell has a fresh orange, rot it.
                    if 0 <= i < rows and 0 <= j < columns and grid[i][j] == 1:
                        fresh -= 1
                        grid[i][j] = 2
                        queue.append((i, j))
        print(grid)
        return minutes if fresh == 0 else -1
        