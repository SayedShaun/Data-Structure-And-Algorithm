def insertion_sort(arr):
    if len(arr) <= 1:
        return arr
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            temp = arr[j]
            arr[j] = arr[j - 1]
            arr[j-1] = temp
            j -= 1

    return arr


arr1 = [2, 4, 3, 5, 1, 6]
print(insertion_sort(arr1))
