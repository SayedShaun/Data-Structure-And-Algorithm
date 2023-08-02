def linear_search(arr, item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i
    return "Not found"


arr = [45, 6, 57, 67, 4, 5, 809, 3]
result = linear_search(arr, 57)
print(result)
