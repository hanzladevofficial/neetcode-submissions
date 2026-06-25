class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {')':'(','}':'{',']':'['}
        opening_brackets = {'(','{','['}
        for c in s :
            if c in opening_brackets :
                stack.append(c)
            else :
                if stack and brackets[c] == stack[-1]:
                    stack.pop()
                else :
                    return False
        if len(stack) == 0:
            return True   


        return False
