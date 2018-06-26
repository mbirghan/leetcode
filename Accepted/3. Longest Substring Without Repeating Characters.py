class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        lwindow = 0
        currentStart = 0
        insideWindow = {}
        
        for i in range(0, len(s)):
            if(s[i] in insideWindow and currentStart <= insideWindow[s[i]]):
                currentStart = insideWindow[s[i]]+1
                insideWindow[s[i]] = i
            else:
                insideWindow[s[i]] = i
            
            if(i - currentStart +1 > lwindow):
                lwindow = i - currentStart +1
        
        return lwindow
