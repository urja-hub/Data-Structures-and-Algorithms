from typing import List
from collections import defaultdict


# time complexity = O(n^2)
#space = O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = defaultdict(int)
        unique_vals = set(nums)
        count = 0
        # itterating through each num to get the count
        for i in unique_vals:
            for j in nums:
                if i == j:
                    count +=1
            freq_dict[i] = count
            count = 0
        
        sorted_freq_dict = dict(sorted(freq_dict.items(), key = lambda item: item[1]))
        keys = list(sorted_freq_dict.keys())
        return(keys[len(keys) - k :])

solution = Solution()
nums = [7,7]
k = 1
ans = solution.topKFrequent(nums,k)
print(ans)


# Alternative methods

# Time complexity: O(n log n)
# Space complexity: O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
    
# Alternative method 2

# Time complexity: O(n log k)
# Space complexity: O(n + k)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
    
# Alternative Method 3 - Best method (Bucket Sort)

# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
                               