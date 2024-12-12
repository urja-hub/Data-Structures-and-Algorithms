def bubbleSort(nums):
    for i in range (len(nums) - 1, 0, -1):
        for j in range(0,i):
            #print(i,j, nums[i], nums[j])
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]

    return nums

nums = [2,4,3,1]
print(bubbleSort(nums))

#time complexty : O(n^2)
#space cpmplexity : O(1)