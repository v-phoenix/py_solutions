'''
Created on Feb 16, 2015

@author: Vinodh Periyasamy
'''

def max_subarray(A):
    global_max = 0
    local_max = 0
    for i in A:
        local_max = max(0, (local_max + i));
        global_max = max(global_max, local_max);
    
    return global_max   
        
    
    