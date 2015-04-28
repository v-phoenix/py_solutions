'''
Created on Apr 23, 2015

@author: Vinodh Periyasamy
'''

'''
Priority Queue : It is a data structure to store a set of S elements each with an associated value called key

Supporting following operations on the Set

Insert (S, x)

Maximum(S)

Extract_Max(S)

Increase_Key(S,x,k) 

'''

negative_infinity = float("-inf")

from algos.sort.sort_functions import max_heapify

def heap_maximum(A):
    return A[0];

def extract_max(A):
    if len(A) < 1:
        raise ValueError('Heap is Empty!');
    
    max_val = A[0];
    A[0] = A[len(A)-1];
    # remove the element from the array
    del A[len(A)-1];
    
    max_heapify(A, 0, len(A)-1);
    return max_val, A;

def heap_increase_key(A,i,key):
    if A[i] > key:
        raise ValueError('key is less than the current key!');
    
    A[i] = key;
    
    while i > 0 and (A[i//3] < A[i]):
        temp = A[i//3]
        A[i//3] = A[i]
        A[i] = temp;
        i = i // 3
     
    return A;   
        
def max_heap_insert(A, key):
    A[len(A)] = negative_infinity
    heap_increase_key(A, len(A), key);
    
    