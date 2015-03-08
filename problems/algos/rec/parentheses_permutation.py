'''
Created on Mar 7, 2015

For a given integer N, this prints all possible permutations of fully balanced parentheses.

Example: 3

()
(())  ()()   
((()))  (()())  (())()  ()(())  ()()()

@author: Vinodh Periyasamy
'''


def brackets(N):
    for i in range(1,N+1):
        brackets_internal("", 0 , 0 , i)
        

def brackets_internal(text, opn, cls, pair):
    if(opn == pair and cls == pair):
        print(text)
    else:
        if(opn < pair):
            brackets_internal(text+"(", opn+1, cls, pair)
        if(cls < opn):
            brackets_internal(text+")", opn, cls+1, pair)   
        
            