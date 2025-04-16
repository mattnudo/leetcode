#https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

def shipWithinDays(self, weights: List[int], days: int) -> int:
        def shippable(capacity):
            daysToShip = 1
            total = 0
            for weight in weights:
                total += weight
                if(total > capacity):
                    daysToShip +=1
                    total = weight
                    if(daysToShip > days):
                        return False
            return True
        left, right = max(weights), sum(weights)
        while (left < right):
            mid = (left + right) // 2
            if(shippable(mid)):
                right = mid
            else:
                left = mid + 1
        return left

#output: least weight capacity shipped within x days given serial loads in weights
#left max(weight), right sum(weights)

print(shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))#15
print(shipWithinDays([3,2,2,4,1,4],3))#6
print(shipWithinDays([1,2,3,1,1],4))#3