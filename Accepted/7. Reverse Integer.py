class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        newNumber = 0
        absX = abs(x)
        isNegativ = absX != x
        
        
        while absX > 0:
            num = absX % 10
            absX -= num
            absX /= 10
            
            newNumber *= 10
            newNumber += num

        if(newNumber > 2147483648 or (newNumber > 2147483647 and not isNegativ)):
            return 0
            
        if(isNegativ):
            newNumber = -newNumber
            
        return newNumber


s = Solution()
print s.reverse(1534236469)