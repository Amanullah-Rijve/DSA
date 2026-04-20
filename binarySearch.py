def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # found
        elif arr[mid] < target:
            left = mid + 1  # go right
        else:
            right = mid - 1  # go left

    return -1  # not found


# Example
arr = [1, 3, 5, 7, 9]
target = 7

result = binary_search(arr, target)

if result != -1:
    print("Found at index:", result)
else:
    print("Not found")