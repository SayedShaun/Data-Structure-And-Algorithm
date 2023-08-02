# 1st method
def quick_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr

    pivot = arr[-1]
    right = []
    left = []
    for i in range(length - 1):
        if arr[i] > pivot:
            right.append(arr[i])
        else:
            left.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)


arr1 = [2, 1, 1000, -9, 4, 3, 7, 5, 6]
print(quick_sort(arr1))


# 2nd method
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr.pop()
    right = []
    left = []
    for i in arr:
        if i > pivot:
            right.append(i)
        else:
            left.append(i)

    return quick_sort(left) + [pivot] + quick_sort(right)


arr1 = [2, 1, 1000, -9, 4, 3, 7, 5, 6]
print(quick_sort(arr1))
