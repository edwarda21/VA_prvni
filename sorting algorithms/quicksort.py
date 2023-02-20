def partition(to_sort):
    pivot = to_sort[0]
    left = 0
    right = len(to_sort) - 1
    while left < right:
        while to_sort[left] < pivot:
            left += 1
        while to_sort[right] > pivot:
            right -= 1
        to_sort[left], to_sort[right] = to_sort[right], to_sort[left]
    print(to_sort[:left])
    print(to_sort[right+1:])
    return to_sort[:left],to_sort[right+1:],left



def quicksort(to_sort):
    print("QS")
    print(to_sort)
    print(len(to_sort))
    if len(to_sort) == 1:
        return to_sort
    else:
        left, right, pivot = partition(to_sort)
        return quicksort(left) + pivot + quicksort(right)


print(quicksort([8,849,48,1,8,97,0,54,48,23,12]))