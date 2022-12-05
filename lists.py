def partition(list_to_sort):
    left_pointer = 0
    right_pointer = len(list_to_sort)-2
    print(list_to_sort[right_pointer])
    buffer_val = list_to_sort[right_pointer+1]
    while right_pointer > left_pointer:
        print(left_pointer)
        while list_to_sort[left_pointer] < list_to_sort[right_pointer]:
            left_pointer += 1
            print(left_pointer)
        while list_to_sort[right_pointer] > list_to_sort[left_pointer]:
            right_pointer -= 1
            print(right_pointer)


partition([7489,5,4684,7646,12,31,2,35,8,4,8,9,6,64,3])
