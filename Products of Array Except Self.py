import numpy as np
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_new = np.array(nums)
        for i in range(len(nums)):
            unchanged_num = nums[i]
            nums_new = nums_new * unchanged_num
            nums_new[i] = unchanged_num
            print("i:",i,"nums: ", nums_new, 'nums[i]', unchanged_num)
        return nums_new
    
solution = Solution()
nums = [1,2,4,6]
print(solution.productExceptSelf(nums))