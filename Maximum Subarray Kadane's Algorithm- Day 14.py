from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currSum = 0

        for n in nums:
            if currSum < 0:
                currSum = 0
            currSum += n
            maxSub = max(maxSub, currSum)

        return maxSub
    

nums = [2,-3,4,-2,2,1,-1,4]
solution = Solution()
print(solution.maxSubArray(nums))