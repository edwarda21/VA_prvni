def partition(in_list):
    left = 0
    right = len(in_list) - 2
    buffer = in_list[-1]
    # initializes left and right pointers along with the buffer that the list will be compared with
    sorted = False
    while not sorted:
        while left < right:
            if in_list[left] < buffer:
                left += 1
            else:
