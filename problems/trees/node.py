'''
Created on Feb 28, 2015

@author: vinodhkps
'''

class BinaryNode:
    '''
    classdocs
    '''

    def __init__(self, dataValue):
        self.__dataValue = dataValue
        self.left = None
        self.right = None
        
    def setLeft(self, left):
        self.left = left
     
    def setRight(self, right):
        self.right = right
        
    def right(self):
        return self.right;
    
    def left(self):
        return self.left;
    
    @property
    def __dataValue__(self):
        return self.__dataValue
    
    def __str__(self, level = 0):
        return 'value of the node {} left : [{}] and right : [{}]'.format(self.__dataValue, self.left, self.right);
    