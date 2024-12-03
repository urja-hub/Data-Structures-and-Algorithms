# time complexity: O(n)
# memory complexity : O(n/2)??

from typing import List

class solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0: return False
        s = list(s)
        brackets = {']':'[','}':'{',')':'('}
        stack = []

        for i in range(0,len(s)):
            if s[i] not in brackets.keys():
                stack.append(s[i])
            elif stack[-1] == brackets[s[i]]:
                stack.pop()
            else: return False
        return True
    
solution = solution()
s="([{}])"
res = solution.isValid(s)
print(res)