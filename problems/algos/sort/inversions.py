'''
Created on Mar 9, 2015

@author: Vinodh Periyasamy


Inversion Count of an Array:

Let A[1..n] be an array of n distinct numbers. If i < j and A[i] > A[j], then 
the pair (i,j) is an inversion of the array A

Reference: CLRS 2-4

'''

# Takes O(n^2)
def brute_force_inversion_count(A):
    inv_count = 0;
    pair = ''
    for i in range(0,len(A)):
        for j in range(i+1, len(A)-1):
            if(A[i] > A[j]):
                inv_count += 1;
                pair += ' ({},{}) '.format(i,j)+';'
    print pair
    return inv_count;

# Takes O(n lg n)
def inversion_count_using_merge_sort(A):
    print('merge_sort incoming Array {}'.format(A))
    return __merge_sort_divide(A,0,(len(A)-1))    
    print('merge_sort sorted Array {}'.format(A))

def __merge_sort_divide(A, p ,r):
    inv_count = 0;
    if(p < r):
        q = (p+r)//2
        inv_count = __merge_sort_divide(A, p, q)
        inv_count += __merge_sort_divide(A, q+1, r)
        inv_count += __merge(A, p , q, r)
        
    return inv_count    
        
def __merge(A,p,q,r):
    inv_count = 0;
    n1 = q - p + 1;
    n2 = r - q;
    B = []
    C = []
    for i in range(0,n1):
        B.append(A[p+i])
    for j in range(0,n2):
        C.append(A[q+j+1])   
    B.append(float("inf"))
    C.append(float("inf"))
    i = 0;
    j = 0;
    for k in range(p,r+1):
        if B[i] <= C[j]:
            A[k] = B[i]
            i = i + 1
        else:
            A[k] = C[j]
            j = j+1
            inv_count = inv_count + 1;
            
    return inv_count;        

    
    
            