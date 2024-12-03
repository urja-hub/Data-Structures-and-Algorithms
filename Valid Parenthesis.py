# time complexity: O(n)
# memory complexity : O(n/2)??

from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1: return False
        s = list(s)
        brackets = {']':'[','}':'{',')':'('}
        stack = []

        for i in range(0,len(s)):
            if s[i] not in brackets.keys():
                stack.append(s[i])
            elif stack and stack[-1] == brackets[s[i]]:
                stack.pop()
            else: return False
        return len(stack) == 0 
    
solution = Solution()
s="([{}])"
res = solution.isValid(s)
print(res)
