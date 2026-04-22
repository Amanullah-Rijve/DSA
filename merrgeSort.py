def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # base case

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])   # left half
    right = merge_sort(arr[mid:])  # right half

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    # compare elements and merge
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Example
arr = [5, 3, 7, 1, 4]
sorted_arr = merge_sort(arr)

print("Sorted:", sorted_arr)