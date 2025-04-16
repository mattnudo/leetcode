#https://algo.monster/liteproblems/542
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
            returns a matrix representing the distance of the nearest 0 for each cell
        """
        #need to traverse all cells
        #searching from a root for the shortest path, bfs with a queue makes sense
        #need a result array that matches the dimension of mat
        #need to keep track of nodes visited
        #need to traverse the queue until all nodes are visited
        rows, columns = len(mat), len(mat[0])
        result = [ [-1] * columns for _ in range(rows) ]
        queue = deque()
        #set the zero locations
        for x in range(rows):
            for y in range(columns):
                if(mat[x][y] == 0):
                    result[x][y] = 0
                    queue.append((x,y))

        neighbours = ((0,1), (0,-1), (1,0), (-1,0))

        while queue:
            i, j = queue.popleft()
            for neighbour_x, neighbour_y in neighbours:
                current_x, current_y = i+neighbour_x, j+neighbour_y
                #if in range
                if( (0 <= current_x < rows) and 0 <= current_y < columns and result[current_x][current_y]==-1):
                       result[current_x][current_y] = result[i][j] +1
                       queue.append((current_x, current_y))

        return result
