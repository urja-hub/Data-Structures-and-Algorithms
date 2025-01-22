# using integration symbol to separate the words and converting them into a single string.\


from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "⨏⨏⨏⨏"
        return '⨏⨏'.join(strs)

    def decode(self, s: str) -> List[str]:
        if s=="⨏⨏⨏⨏":
            return []
        return s.split('⨏⨏')

solution = Solution()
strs = ['a','b','c']
ans = solution.encode(strs)
print(ans)
print(solution.decode(ans))

