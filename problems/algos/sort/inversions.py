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

    
    
            