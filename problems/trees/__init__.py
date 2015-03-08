from node import BinaryNode
from binarytree import BinarySearchTree
import sys


aNode = BinaryNode(89)
anotherNode = BinaryNode(99)
oneAnotherNode = BinaryNode(100)
smallNode = BinaryNode(80)
x = BinaryNode(83)
y = BinaryNode(75)

a_tree = BinarySearchTree()
a_tree.__addnode__(aNode)
a_tree.__addnode__(anotherNode)
a_tree.__addnode__(oneAnotherNode)
a_tree.__addnode__(smallNode)
a_tree.__addnode__(x)
a_tree.__addnode__(y)

sys.stdout.write('In Order: ') 
a_tree.__inorder__()
print('')
sys.stdout.write('Pre Order: ')
a_tree.__preorder__()
print('')

print(a_tree.root())

