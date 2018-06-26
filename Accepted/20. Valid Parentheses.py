class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        for i in s:
            if(i == "(" or i == "[" or i == "{"):
                stack.append(i)
            else:
                if(len(stack) <= 0):
                    return False
                j = stack.pop()
                if(i == ")" and j == "("):
                    continue
                elif(i == "}" and j == "{"):
                    continue
                elif(i == "]" and j == "["):
                    continue
                else:
                    return False
                
        return len(stack) == 0
            