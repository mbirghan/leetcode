class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        rnge = 9
        digits = 1
        nbrStart = 1

        while n > rnge*digits:
            n -= rnge*digits
            digits += 1
            rnge *= 10
            nbrStart *= 10
        
        number = (n-1)/digits
        digitInNumber = (n-1) % digits
        nbrStart += number
        
        digit = (nbrStart / 10**(digits-digitInNumber - 1)) % 10


        return digit

s = Solution()
print s.findNthDigit(189)

