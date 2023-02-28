def merge(arr):
    separator = (len(arr)) // 2
    left_side = arr[:separator]
    right_side = arr[separator:]
    len_of_left = len(left_side)
    len_of_right = len(right_side)
    l = 0
    r = 0
    insert = 0
    while l < len_of_left and r < len_of_right:
        if left_side[l] < right_side[r]:
            arr[insert] = left_side[l]
            l += 1
        else:
            arr[insert] = right_side[r]
            r += 1
        insert += 1

    while l < len_of_left:
        arr[insert] = left_side[l]
        insert += 1
        l += 1
    while r < len_of_right:
        arr[insert] = right_side[r]
        insert += 1
        r += 1
    return arr


def mergeSort(array):
    if len(array) < 2:
        return array
    separator = (len(array)) // 2
    left_side = array[:separator]
    right_side = array[separator:]

    left_sorted = mergeSort(left_side)
    right_sorted = mergeSort(right_side)
    return merge(left_sorted + right_sorted)

print(mergeSort([1,12,48,654,53,37,-1,2]))
