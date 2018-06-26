class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.rekIsMatch(s, p, {})
        
    
    def rekIsMatch(self, s, p, patternPoint):
        res = False
        star = False
        pattern = ""
        newP = p

        if(p in patternPoint):
            if(patternPoint[p] == s):
                return False
        
        if(len(p) >= 1):
            pattern = p[0]
            newP = p[1:]
            if(len(p) >= 2):
                if(p[1] == "*"):
                    star = True
                    newP = p[2:]
                    
        if(len(p) == 0 and len(s) != 0):
            return False
          
        if(len(s) == 0 and len(p) == 0):
            return True
        elif(len(s) == 0 and star):
            return self.isMatch(s, newP)
        elif(len(s) == 0):
            return False
        

            
        
        if(s[0] == pattern or pattern == "."):
            if(star):
                resA = self.rekIsMatch(s[1:], p, patternPoint)
                
                if(resA):
                    return True
                
                resB = self.rekIsMatch(s, newP, patternPoint)
                
                res = resA or resB
            else:
                res = self.rekIsMatch(s[1:], newP, patternPoint)
        elif(star):
            res =  self.rekIsMatch(s, newP, patternPoint)
        

        if(not res):
            patternPoint[p] = s
           
        return res
