class Solution:
    def isHappy(self, n: int) -> bool:
        #turn an int into a string and split it
        def splitNumber(digit:int) :
            return [int(number) for number in str(digit)]

        sum_digits = n
        results = []

        while True:
            digits = splitNumber(sum_digits)#split the number into its parts
            sum_digits = 0
            for num in digits:
                sum_digits += num ** 2
                #how to escape infinite loop? fast/slow?
            if(sum_digits in results):
                return False
            results.append(sum_digits)
            if(sum_digits == 1 ):
                return True
        return False
