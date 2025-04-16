class Solution:
    def climbStairs(self, n: int) -> int:
        """
            how many ways can you climb to the top of the stairs given the choice of 1 or 2 steps at a time?
        """
        previous, current = 0, 1
        for step in range(n):
            previous, current = current , current + previous
        return current