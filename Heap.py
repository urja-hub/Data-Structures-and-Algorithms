# Create a function for heap 

def create_max_heap(arr):
    arr.insert(0,0)
    for i in range(1, len(arr)):

        current = i
        while current > 1 and arr[current] > arr[current//2]:
            arr[current],arr[current//2] = arr[current//2],arr[current]
            current = current//2

    arr.pop(0)
    return arr

''' while j < len(arr):
        if arr[i] > arr[i//2]:
            arr[i],arr[i//2] = arr[i//2],arr[i]
            i = i//2
        
        else:
            j += 1
            i = j'''
    
'''
    for i in range(2, len(arr)):
        if arr[i] > arr[i//2]:
            arr[i],arr[i//2] = arr[i//2],arr[i]
    return arr[1:]
'''
arr = [1,2,3,4,5,93,23,0,43]
print(create_max_heap(arr))