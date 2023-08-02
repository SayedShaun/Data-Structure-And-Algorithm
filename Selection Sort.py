def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp

    return arr

arr = [2,100,-45, 45456, 5, 1, 6, 4, 3]
print(selection_sort(arr))
