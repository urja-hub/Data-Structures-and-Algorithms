from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) - 1

        while i <= j:
            if nums[i] == val:
                nums[i] = nums[j]
                nums[j] = '_'
                j -= 1
            else:
                i += 1
        return i


nums = [0,1,2,2,3,0,4,2]
val = 2

solution = Solution()
print(solution.removeElement(nums, val))

#method 1
class Solution:
    def removeElement1(self, nums: List[int], val: int) -> int:
        seen = []
        for i in range(len(nums)):
            if nums[i] != val:
                seen.append(nums[i])
        return seen
