class Solution:
    def factorial(self, n: int) -> int:
        if n == 1 or n == 0:
            return 1
        return n * self.factorial(n-1)


print(Solution().factorial(4))
#test_case_1
expected, nums = 120, 5
actual = Solution().factorial(nums)
assert expected==actual, "Mistake in test case 1"
#test_case_2
expected, nums = 24, 4
actual = Solution().factorial(nums)
assert expected==actual, "Mistake in test case 2"


class Solution:
    def __init__(self):
        self.memo = {}  # Dictionary to store computed factorial values

    def factorial(self, n: int) -> int:
        if n in self.memo:  # Check if result is already computed
            return self.memo[n]
        if n == 0 or n == 1:  # Base cases
            return 1
        # Compute factorial and store it in memo dictionary
        self.memo[n] = n * self.factorial(n - 1)
        return self.memo[n]
