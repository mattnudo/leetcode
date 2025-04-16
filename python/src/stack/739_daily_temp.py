class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize a list of zeros for the answer with the same length as the input list
        answer = [0] * len(temperatures)
        # Initialize an empty list to be used as a stack to keep track of temperatures indices
        stack = []
      
        # Enumerate over the list of temperatures
        for index, current_temp in enumerate(temperatures):
            # Loop through the stack as long as it's not empty and the current temperature
            # is greater than the temperature at the index of the last element in the stack
            while stack and temperatures[stack[-1]] < current_temp:
                # Pop the index of the temperature that is less than the current temperature
                previous_index = stack.pop()
                # Calculate the number of days between the previous and current temperature
                # and update the answer list
                answer[previous_index] = index - previous_index
          
            # Append the current index to the stack
            stack.append(index)
      
        # Return the answer list which contains the number of days to wait until a warmer temperature
        return answer