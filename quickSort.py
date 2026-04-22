def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # base case

    pivot = arr[0]  # choose first element as pivot

    smaller = []
    equal = []
    greater = []

    for x in arr:
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)

    return quick_sort(smaller) + equal + quick_sort(greater)


# Example
arr = [5, 3, 7, 1, 4]
sorted_arr = quick_sort(arr)

print("Sorted:", sorted_arr)