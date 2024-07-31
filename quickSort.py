def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

# 示例用法
arr = [3, 6, 8, 10, 1, 2, 1]
print("原始数组:", arr)
sorted_arr = quicksort(arr)
print("排序后数组:", sorted_arr)
