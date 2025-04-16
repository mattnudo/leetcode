class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
            calculates the integer of the RPN expression contained in tokens

            Parameters
            ------
            tokens: list[str]
                tokens to calculate
            Returns
            ------
            int : integer of RPN calculation
        """
        number_stack = []
      
        # Loop over each token in the input list
        for token in tokens:
            # If the token represents a number (accounting for negative numbers)
            if len(token) > 1 or token.isdigit():
                # Convert the token to an integer and push it onto the stack
                number_stack.append(int(token))
            else:
                # Perform the operation based on the operator
                if token == "+":
                    # Pop the last two numbers, add them, and push the result back
                    number_stack[-2] += number_stack[-1]
                elif token == "-":
                    # Pop the last two numbers, subtract the second from the first, and push back
                    number_stack[-2] -= number_stack[-1]
                elif token == "*":
                    # Pop the last two numbers, multiply, and push the result back
                    number_stack[-2] *= number_stack[-1]
                else: # Division
                    # Ensure integer division for negative numbers too
                    number_stack[-2] = int(float(number_stack[-2]) / number_stack[-1])
                # Pop the last number (second operand) from the stack as it's been used
                number_stack.pop()
      
        # Return the result which is the only number left in the stack
        return number_stack[0]
