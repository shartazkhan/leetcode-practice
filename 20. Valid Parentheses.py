class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic_of_par = {')':'(','}':'{',']':'['}

        for item in s:
            if item in dic_of_par:
                if stack and stack[-1] == dic_of_par[item]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(item)

        return True if not stack else False
