import heapsort
import mergesort
import quicksort
import time
import random
array = [random.randint(-999999, 999999) for iter in range(1000001)]

#quicksort time
qs_ts = time.process_time()
quicksort.quicksort(array)
qs_te = time.process_time()
qs_time = qs_te - qs_ts

#mergesort time
ms_ts = time.process_time()
mergesort.mergeSort(array)
ms_te = time.process_time()
ms_time = ms_te - ms_ts

#heapsort time
hs_ts = time.process_time()
#heapsort.Heap(array).sort()
hs_te = time.process_time()
hs_time = hs_te - hs_ts

print(f"The time for quicksort is {qs_time}")
print(f"The time for mergesort is {ms_time}")
print(f"The time for heapsort is {hs_time}")
