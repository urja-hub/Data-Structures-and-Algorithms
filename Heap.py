# Create a function for heap 
# This is almost good for now, but check how can you make it to original index and check for alternative solutions as well.
# Remember I'm doing the heapify up(top - down approach) procedure, code for heapify down, or bottom up approach
def create_max_heap(arr):
    arr.insert(0,0)
    for i in range(1, len(arr)):

        current = i
        while current > 1 and arr[current] > arr[current//2]:
            arr[current],arr[current//2] = arr[current//2],arr[current]
            current = current//2

    arr.pop(0)
    return arr

# Create a function to delete the elements

def delete_element(arr):

    arr.insert(0,0)
    arr[1] = arr[-1]
    arr.pop()
    current = 1
    while 2 * current < len(arr):
        if 2 * current + 1 < len(arr):
            if arr[2 * current] > arr[2 * current +1]:
                if arr[2 * current] > arr[current]:
                    arr[2*current], arr[current] = arr[current], arr[2 * current]
                    current = 2 * current
                else:
                    break
            else:
                if arr[2*current] < arr[2*current + 1]:
                    arr[2*current + 1], arr[current] = arr[current], arr[2 * current + 1]
                    current = 2 * current + 1
                else: 
                    break
        
        else:
            if arr[2 * current] > arr[current]:
                arr[2 * current], arr[current] = arr[current],arr[2 * current]
            
            break

        

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
print(delete_element(arr))