#time complexity : n
#space complexity : n

def stalin_sort(nums):
    nums_sorted = [nums[0]]
    for i in range(1, len(nums)): 
        if nums[i] >= nums_sorted[-1]:
            nums_sorted.append(nums[i])
    return nums_sorted

ls = [1, 4, 2, 8, 11, 13, 15, 100, 39, 45, 50]
expected = [1, 4, 8, 11, 13, 15, 100]
actual = stalin_sort(ls)
assert expected == actual, "Mistake in test case 1"
print('OK')


def stalin_sort_in_place(nums):
    i = 1
    while i < len(nums):
        if nums[i] < nums[i - 1]:
            nums.pop(i)
        else:
            i += 1
    return nums