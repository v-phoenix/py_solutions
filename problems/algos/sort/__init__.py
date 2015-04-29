from sort_functions import insertion_sort
from sort_functions import merge_sort
from sort_functions import bubble_sort
from inversions import brute_force_inversion_count
from inversions import inversion_count_using_merge_sort
from sort_functions import heap_sort;
from sort_functions import build_max_heap;
from sort_functions import quick_sort;

B = [4,7,3,5,2,1,9,6]

# B = [4,7,3]

# print('Merge Sort :')
# merge_sort(B)
# 
# print('Insertion Sort :')
# insertion_sort(B)

# bubble_sort(B)

# heap_sort(B);

quick_sort(B);

# A, heap_size = build_max_heap(B, 3);
# print('Max heap is {} & heap size is {} '.format(A,heap_size));


#print('Brute Force: Inversion Count of {} is {} '.format(B, brute_force_inversion_count(B)))

#print('Optimized Inversion Count: Inversion Count of {} is {} '.format(B, inversion_count_using_merge_sort(B)))