def sort_and_merge(arr, left, mid, right):
    # Count the number of elements
    n1= mid -left + 1
    n2 = right - mid

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 +j]
    

    i, j, k = 0, 0, left

    while i < n1 & j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else: 
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] =  R[j]
        j += 1
        k += 1

def print_arr(arr):
    for i in arr:
        print(i, end = ' ')

def merge_sort(arr, left, right):
    
    if left < right:
        mid = (left + right) //2  # this will only work for 2 or more elements

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        sort_and_merge(arr, left, mid, right)

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print_arr(arr)

    print(merge_sort(arr, 0, len(arr)-1))