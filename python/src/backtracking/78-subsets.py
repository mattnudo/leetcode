class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
            Returns all possible subsets of nums
            Parameters
            ------
            nums (List[int]): list of numbers

            Returns
            ------
            list of lists containing all possible subsets of nums
        """
        result = []
        #seems like a backtracking problem
        #recursion on nums starting on 0th element
        def backtrack(start, path):
            result.append(path[:])
            #for all elements in nums from start to end
            for x in range(start, len(nums)):
                #append the number to the path
                path.append(nums[x])
                #recurse 
                backtrack(x+1, path)
                path.pop()

        backtrack(0, [])
        return result
