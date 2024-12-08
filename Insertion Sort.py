# Insertion Sort
# Please implement the function which takes as an input list of numbers and returns the sorted list
# Use Insertion Sort algorithm

# time complexity: O(n^2)
#space complexity: O(1)
def insertion_sort(nums):
    for i in range(1,len(nums)):
        for j in range(0,i):
            if nums[i] < nums[j]:
                nums.insert(j, nums[i])
                del nums[i + 1]
                break
    return nums

# testing code
# do NOT modify testing code below

def test_sorting(sorting_algorithm):
    nums = [5,4,3,2,10]
    expected = [2,3,4,5,10]
    actual = sorting_algorithm(nums)
    assert expected == actual, "Mistake in implementation"
# if your implementation is correct, you should see "OK"
# if your implementation is not correct, you will see "Mistake in implementation"
test_sorting(insertion_sort)
print('OK')
