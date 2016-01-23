from pythonds.trees.binaryTree import BinaryTree
from pythonds.basic.stack import Stack
import operator

def buildParseTree(fpexp):
    fplist = fpexp.split()
    st = Stack()
    bt = BinaryTree('')
    st.push(bt)
    current = bt
    for i in fplist:
        if i == '(':
            current.insertLeft('')
            st.push(current)
            current = current.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            current.setRootVal(int(i))
            current = st.pop()
        elif i in ['+', '-', '*', '/']:
            current.setRootVal(i)
            current.insertRight('')
            st.push(current)
            current = current.getRightChild()
        elif i == ')':
            current = st.pop()
        else:
            raise "invalid input"
    return bt

def evaluate(bt):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    left = bt.getLeftChild()
    right = bt.getRightChild()

    if left and right:
        fn = opers[bt.getRootVal()]
        return fn(evaluate(left), evaluate(right))
    else:
        return bt.getRootVal()

def preorder(tree):
    if tree:
        print tree.getRootVal()
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

def inorder(tree):
  if tree != None:
      inorder(tree.getLeftChild())
      print(tree.getRootVal())
      inorder(tree.getRightChild())



pt = buildParseTree("( ( 10 + 5 ) * 3 )")
pt.postorder()