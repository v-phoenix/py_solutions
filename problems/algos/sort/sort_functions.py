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
                        
                
        
