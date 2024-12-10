def selection_sort(nums):
    for i in range(len(nums)):
        index = i
        current_min = nums[i]
        for j in range(i + 1, len(nums)):
            if nums[j] < current_min:
                current_min = nums[j]
                index = j
        nums[index] = nums[i]
        nums[i] = current_min
    return nums

def test_sorting(sorting_algorithm):
    nums = [5, 4, 3, 2, 10]
    expected = [2, 3, 4, 5, 10]
    actual = sorting_algorithm(nums)
    assert expected == actual, "Mistake in implementation"

test_sorting(selection_sort)
print('OK')
