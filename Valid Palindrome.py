import re

class Solution:
    def isPalindrome(self, s:str) -> bool:
        s = re.sub(r'[^A-Za-z0-9]+','',s)
        print(s)
        s = s.replace(" ","")
        s = s.lower()
        print(s)
        if s == s[::-1]: return True
        else: return False

solution = Solution()
s = "Was += i=t a * car or# a cat I saw?"
print(solution.isPalindrome(s))