class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
            returns the point closest to the origin

            Parameters: 
            points (List[List[int]]): points to calculate distance
            k (int): return k closest points from origin

            returns:
            returns the point closest to the origin
        """
        # Sort the given list of points by their Euclidean distance
        # from the origin (0, 0) without actually computing the square root.
        # The lambda function computes the squared distance.
        points.sort(key=lambda x: x[0]**2 + x[1]**2)
      
        # Return the first k points from the sorted list.
        return points[:k]
        