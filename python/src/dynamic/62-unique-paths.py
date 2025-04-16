class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
            return the # of possible unique paths from m to n
        """
        # Initialize a list that will hold the number of unique paths to each cell
        # in the first row. Initially, there's only one unique path to reach any cell
        # in the first row since the only possible move is to the right.
        path_counts = [1] * n
        print(path_counts)
      
        # Iterate over the rows of the grid starting from the second row,
        # since the first row has been initialized already.
        for row in range(1, m):
            # Iterate over the columns starting from the second column,
            # since the first column only has one unique path (move down).
            for col in range(1, n):
                # The number of unique paths to reach this cell is the sum of
                # the number of unique paths to reach the cell directly above
                # and the number of unique paths to reach the cell to the left.
                path_counts[col] += path_counts[col - 1]
                print(path_counts)
      
        # Return the number of unique paths to reach the bottom-right corner of the grid,
        # which is the last element in the path_counts list.
        return path_counts[-1]