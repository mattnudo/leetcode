class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        'return the fewest number of coins necessary to make up amount
        '''
        #O(n+m)
        # num_coins[i] will be storing the minimum number of coins required for amount i
        # num_coins[0] is 0 because no coins are needed for the amount 0
        num_coins = [0] + [amount+1] * amount
      
        # Traverse through all the amounts from 1 to amount inclusive
        for coin in coins:  # For each coin
            for current_amount in range(coin, amount + 1):
                # Update the dp table by comparing the current value
                # with the value if we include the current coin
                num_coins[current_amount] = min(num_coins[current_amount], num_coins[current_amount - coin] + 1)
      
        #print(num_coins)
        # If we have not found a combination to form the amount
        # then num_coins[amount] will > amount
        return -1 if num_coins[amount] > amount else num_coins[amount]
