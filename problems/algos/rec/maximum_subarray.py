'''
Created on Mar 14, 2015

@author: Vinodh Periyasamy
'''


def brute_force_max_subarray(A):
    max_sum = 0;
    sequence_start = -1
    sequence_end = -1
    for i in range(0,len(A)):
        local_sum = 0
        for j in range(i, -1, -1):
            local_sum += A[j];
            if(local_sum > max_sum):
                max_sum = local_sum
                sequence_start = j
                sequence_end = i
    print ('max sum in the given array is {} and the sequence starts from {} and ends at {}'.format(max_sum, sequence_start, sequence_end))
    


def find_max_subarray(A):
    low,high,max_value = __find_max_subarray_internal(A, 0, len(A)-1)
    return low,high,max_value
    

def __find_max_subarray_internal(A, low, high):
    if low == high:
        return low, high, A[low]
    else:
        mid = (low + high)/2
        left_low, left_high, left_max = __find_max_subarray_internal(A, low, mid)
        right_low, right_high, right_max = __find_max_subarray_internal(A, mid+1, high)
        cross_low, cross_high, cross_sum = __find_max_sub_crossing_array(A, low, mid, high)
        
        if left_max >= right_max and left_max >= cross_sum:
            return left_low, left_high, left_max
        if right_max >= left_max and right_max >= cross_sum:
            return right_low, right_high, right_max
        return cross_low, cross_high, cross_sum
        
        
def __find_max_sub_crossing_array(A, low, mid, high):
    left_sum_max = float('-inf')
    local_sum = 0;
    for i in range(mid, low-1, -1):
        local_sum += A[i];
        if(local_sum > left_sum_max):
            left_sum_max = local_sum
            max_left = i;
    right_sum_max = float('-inf')
    local_sum = 0;
    for j in range(mid+1, high+1):
        local_sum += A[j]
        if(local_sum > right_sum_max):
            right_sum_max = local_sum
            max_right = j
    
    return max_left, max_right, left_sum_max+right_sum_max
            
    
    
    
            
