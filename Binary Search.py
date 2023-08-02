# program 1
def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    while high >= low:
        mid = (low + high) // 2
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return "Not found"


unsorted_arr = [45, 6, 57, 67, 4, 5, 809, 3]
sorted_arr = sorted(unsorted_arr)
print(sorted_arr)
print(binary_search(sorted_arr, 100))


# program 2
def binary_search(arr, low, high, item):
    if high < low:
        return -1
    mid = (low + high) // 2
    if arr[mid] == item:
        return mid
    elif arr[mid] > item:
        return binary_search(arr, low, mid - 1, item)
    else:
        return binary_search(arr, mid + 1, high, item)


unsorted_arr = [45, 6, 57, 67, 4, 5, 809, 3]
sorted_arr = sorted(unsorted_arr)
print(sorted_arr)
print(binary_search(sorted_arr, 0, len(sorted_arr) - 1, 57))
