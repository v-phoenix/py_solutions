from parentheses_permutation import brackets
from maximum_subarray import brute_force_max_subarray
from maximum_subarray import find_max_subarray

A = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]

# brackets(3)

# brute_force_max_subarray(A);

low, high, value = find_max_subarray(A);

print('max sum in the given array is {} and the sequence starts from {} and ends at {} '.format(value, low, high))
