class Solution:
    def isValid(self, s: str) -> bool:
        stack = []     
        print(stack)
        bracket = {")":"(", "]":"[", "}":"{"}
        for x in s:
            if x in bracket.values():
                stack.append(x)
            elif x in bracket:
                if len(stack) == 0 :
                    stack.append(x)
                elif stack[-1] == bracket[x]:
                    stack.pop()
                else:
                    break
        return True if stack == [] else False
            
