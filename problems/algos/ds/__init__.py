from algos.sort.sort_functions import max_heapify
from algos.sort.sort_functions import build_max_heap
from priority_queue import heap_maximum
from priority_queue import extract_max
from priority_queue import heap_increase_key

B = [4,7,3,5,2,1,9,6]

B, heap_size = build_max_heap(B);

print('Max Heap is {}'.format(B))

print('Max of the heap is {} '.format(heap_maximum(B)))

# max_val, B = extract_max(B);
# print('Max & Heap after extracting max {}, {} '.format(max_val, B))

B = heap_increase_key(B, 1, 10);

print('heap after key increase {} '.format(B))