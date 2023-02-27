def partition(to_sort):
    print("Partition no. ", partition.counter)
    partition.run = 1
    partition.counter += 1
    pivot = to_sort[0]
    left = 1
    right = len(to_sort) - 1
    print("Pivot", pivot)
    while left < right:
        print(f"Partition run No. {partition.run}")
        print("List:", to_sort)
        partition.run +=1
        while to_sort[left] < pivot:
            left += 1
        while to_sort[right] > pivot:
            right -= 1
        if left < right:
            to_sort[left], to_sort[right] = to_sort[right], to_sort[left]
    to_sort[0],to_sort[right] = to_sort[right],pivot
    print("End of partition:")
    print(to_sort)
    return to_sort[:right], to_sort[left+1:], [to_sort[right]]


partition.counter = 1
partition.run = 1


def quicksort(to_sort):
    print("QS")
    if len(to_sort) == 1:
        return to_sort
    else:
        left, right, pivot = partition(to_sort)
        return quicksort(left) + pivot + quicksort(right)


print(quicksort([8, 849, 48, 1, 7, 97, 0, 54, 48, 23, 12]))
