def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)

    merged_arr = []
    i = j = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] > right_arr[j]:
            merged_arr.append(right_arr[j])
            j += 1
        else:
            merged_arr.append(left_arr[i])
            i += 1

    merged_arr.extend(left_arr[i:])
    merged_arr.extend(right_arr[j:])

    return merged_arr


arr = [2, 1, 3, 5, 4, 6]
print(merge_sort(arr))
