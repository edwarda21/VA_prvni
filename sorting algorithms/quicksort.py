def partition(to_sort):
    pivot = to_sort[0]
    left = 0
    right = len(to_sort) - 1
    while left < right:
        while to_sort[left] <= pivot and left < len(to_sort) - 1:
            left += 1
        while to_sort[right] > pivot and right > 0:
            right -= 1
        if left < right:
            to_sort[left], to_sort[right] = to_sort[right], to_sort[left]
    to_sort[0], to_sort[right] = to_sort[right], pivot
    return right


def quicksort(to_sort):
    if len(to_sort) < 2:
        return to_sort
    else:
        pivot_index = partition(to_sort)
        return quicksort(to_sort[:pivot_index]) + [to_sort[pivot_index]] + quicksort(to_sort[pivot_index + 1:])


print(quicksort([8, 849, 48, 1, 7, 97, 0, 54, 23, 12, 69]))

print(quicksort(
    [64, 8, 12, 53, 110, 1, 99, 405, 802, 77, 83, 65, 22, 11, 111, 1111, 9, .8, 8, 8, 8, 64, 64, 69, 69, 5, -69420363,
     69.420636]))
