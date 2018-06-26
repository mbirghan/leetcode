class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num >= 4:
            if(num % 4 != 0):
                return False
            else:
                num = num/4
        
        if(num == 1):
            return True
        else:
            return False

s = Solution()
print s.isPowerOfFour(16)