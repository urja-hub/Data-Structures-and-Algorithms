class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0

expected, n = False, 4
actual = Solution().canWinNim(n)
assert expected == actual, "Mistake in test case 1"

expected, n = True, 2
actual = Solution().canWinNim(n)
assert expected == actual, "Mistake in test case 2"

expected, n = True, 1
actual = Solution().canWinNim(n)
assert expected == actual, "Mistake in test case 3"

print('All tests pass!')
git rebase -i HEAD~4
