from typing import List

class Solution:
    def fib(self, n : int) -> int:

        if n == 0:
            return 0
        if n == 1: 
            return 1
        
        return self.fib(n-1) + self.fib(n-2)
    
#test_case_1
expected, nums = 1, 2
actual = Solution().fib(nums)
assert expected==actual, "Mistake in test case 1"
#test_case_2
expected, nums = 2, 3
actual = Solution().fib(nums)
assert expected==actual, "Mistake in test case 2"
#test_case_3
expected, nums = 3, 4
actual = Solution().fib(nums)
assert expected==actual, "Mistake in test case 2"
