'''
Created on Mar 8, 2015

Contains various sort functions

@author: Vinodh Periyasamy
'''

positive_infinity = float("inf")

def bubble_sort(A):
    print('bubble_sort incoming Array {}'.format(A))
    for i in range(0, len(A)-2):
        for j in range(len(A)-1, i, -1):
            if (A[j] < A[j-1]):
                t = A[j]
                A[j] = A[j-1]
                A[j-1] = t
    print('bubble_sort sorted Array {}'.format(A))
        
        
def insertion_sort(A):
    print('insertion_sort incoming Array {}'.format(A))
    for i in range(1, len(A)):
        key = A[i];
        j = i - 1;
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j = j - 1;
        A[j+1] = key
        
    print('insertion_sort sorted Array {}'.format(A))
    

def merge_sort(A):
    print('merge_sort incoming Array {}'.format(A))
    __merge_sort_divide(A,0,(len(A)-1))    
    print('merge_sort sorted Array {}'.format(A))
    

def heap_sort(A):
    print('heap sort incoming array {}'.format(A));
    d = 2;
    B, heap_size = build_max_heap(A,d);
    for i in range(len(B)-1, 0, -1):
        temp = B[i];
        B[i] = B[0];
        B[0] = temp;
        heap_size = heap_size - 1;
        max_heapify(B,0,d,heap_size);
        
    print('heap sort sorted array {}'.format(B));

def quick_sort(A):
    print('quick sort incoming array {}'.format(A));
    __quicksort(A, 0, len(A) -1);
    print('quick sort sorted array {}'.format(A));    

def __quicksort(A, p , r):
    if(p < r):
        q = __quick_sort_partition(A, p, r);
        __quicksort(A, p, q-1);
        __quicksort(A, q+1, r);


def __merge_sort_divide(A, p ,r):
    if(p < r):
        q = (p+r)//2
        __merge_sort_divide(A, p, q)
        __merge_sort_divide(A, q+1, r)
        __merge(A, p , q, r)
        
def __merge(A,p,q,r):
    n1 = q - p + 1;
    n2 = r - q;
    B = []
    C = []
    for i in range(0,n1):
        B.append(A[p+i])
    for j in range(0,n2):
        C.append(A[q+j+1])   
    B.append(positive_infinity)
    C.append(positive_infinity)
    i = 0;
    j = 0;
    for k in range(p,r+1):
        if B[i] <= C[j]:
            A[k] = B[i]
            i = i + 1
        else:
            A[k] = C[j]
            j = j+1        
                        
                    

def max_heapify(A, i, d, heap_size):
        
    largest = i;
    
    for j in range(1, d+1):
        aChild = d * i + j;
        if(aChild <= heap_size and A[aChild] > A[largest]):
            print('i is {} & its Child location is {}'.format(i, aChild))
            largest = aChild;
    
    if(largest != i):
        temp = A[i];
        A[i] = A[largest];
        A[largest] = temp;
        max_heapify(A, largest, d, heap_size);


def build_max_heap(A, d):
    heap_size = len(A)-1;
    for i in range(heap_size//d, -1, -1):
        max_heapify(A,i,d,heap_size);
    
    return A, heap_size;


def __quick_sort_partition(A, p , r):
    i = p - 1;
    x = A[r];
    for j in range(p, r):
        if(A[j] <= x):
            i = i+1;
            temp = A[i];
            A[i] = A[j];
            A[j] = temp;
    t = A[i+1];
    A[i+1] = A[r];
    A[r] = t;
    return i+1;
    
    
    
