'''
Created on Feb 28, 2015

@author: Vinodh Periyasamy
'''

from node import BinaryNode


class BinarySearchTree(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.__root = None
        
    
    def __addnode__(self, node):
        if(not isinstance(node, BinaryNode)):
            raise ValueError('Cannot Add a Non BinaryNode {}'.format(node))
        if(self.__root is None):
            self.__root = node
        else:    
            self.__add_node_internal(self.__root, node.__dataValue__)
            
    
    def __add_node_internal(self, node, value):
        if(node is None):
            return BinaryNode(value)
        else:    
            if(value <= node.__dataValue__):
                node.left = self.__add_node_internal(node.left, value)
            else:    
                node.right = self.__add_node_internal(node.right, value)
            return node;    
        print('Add Node Internal {}'.format(self.__root))   
        
        
    def root(self):
        return self.__root         
    
    def __inorder__(self):
        self.__inorder_internal(self.__root)
    
    def __inorder_internal(self, node):
        if(node is None):
            return ""
        self.__inorder_internal(node.left)
        print(node.__dataValue__),
        self.__inorder_internal(node.right)                                    
        
        
    def __preorder__(self):
        self.__preorder_internal(self.__root)
    
    
    def __preorder_internal(self, node):
        if(node is None):
            return ""
        print(node.__dataValue__),
        self.__preorder_internal(node.left)
        self.__preorder_internal(node.right)