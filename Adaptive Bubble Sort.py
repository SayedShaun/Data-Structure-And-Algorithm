def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        flag = True
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = False
        if flag is True:
            break
    return arr


arr = [20, 40, 30, 70, 60, 50]
print(bubble_sort(arr))