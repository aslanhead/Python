import unittest

class Node:

    def __init__(self, value):
        self._value = value
        self._right = None
        self._left = None
        self._sibling = None
    
    def Left(self):        
        return self._left
    
    def Right(self):        
        return self._right

    def Sibling(self):        
        return self._sibling
        
    def SetLeft(self, Left):
        self._left = Left
        return self

    def SetRight(self, Right):
        self._right = Right
        return self

    def SetSibling(self, Sibling):
        self._sibling = Sibling
        return self

    def Value(self):
        return self._value

    def SiblingValue(self):
        if self._sibling is None:
            return None
        return self._sibling._value

def PrintTree(root):
    if root is not None:
        message = ""
        if root.Sibling() is not None:
            message = " Sibling " + str(root.SiblingValue())
        print (str(root.Value()) + message)               
        PrintTree(root.Left())        
        PrintTree(root.Right())   


def MapSiblings(root, level, d):
    if root is not None:
        if level in d:
            d[level].SetSibling(root)
        d[level] = root
        MapSiblings(root.Left(), level+1,d)
        MapSiblings(root.Right(), level+1,d)

def Connect(root):    
    while root is not None: 
        currentNodeSibling = root.Sibling()        
        if root.Left() is not None:
            if root.Right() is not None:
                root.Left().SetSibling(root.Right())
        if root.Right() is not None:            
            if currentNodeSibling is not None:        
                leftMost = GetLeftMost(currentNodeSibling)
                root.Right().SetSibling(leftMost)
        if root.Left() is not None:
            root = root.Left()
        elif root.Right() is not None:
            root = root.Right()        
        else:
            root = currentNodeSibling

def GetLeftMost(root):
    while root is not None:        
        if root.Left() is not None:
            return root.Left()
        if root.Right() is not None:
            return root.Right()
        root = root.Sibling()
    
    
class TestSiblingConnect(unittest.TestCase):
    def test_FullTreeUsingConnect(self):
        print("test_FullTreeUsingConnect")
        n1 = Node (1)    
        n2 = Node (2)
        n3 = Node (3)
        n4 = Node (4)
        n5 = Node(5)
        n6 = Node(6)
        n7 = Node(7)
        n1.SetLeft(n2)
        n1.SetRight(n3)
        n2.SetLeft(n4)
        n2.SetRight(n5)
        n3.SetLeft(n6)
        n3.SetRight(n7)
        Connect(n1)
        PrintTree(n1)
    
    def test_MissingLeftNodeUsingConnect(self):
        print("test_MissingLeftNodeUsingConnect")
        n1 = Node (1)    
        n2 = Node (2)
        n3 = Node (3)
        n4 = Node (4)
        n5 = Node(5)
        #n6 = Node(6)
        n7 = Node(7)
        n1.SetLeft(n2)
        n1.SetRight(n3)
        n2.SetLeft(n4)
        n2.SetRight(n5)
        #n3.SetLeft(n6)
        n3.SetRight(n7)
        Connect(n1)
        PrintTree(n1)

    def test_MissingLeftNodeUsingMapSiblings(self):
        print("test_MissingLeftNodeUsingMapSiblings")
        n1 = Node (1)    
        n2 = Node (2)
        n3 = Node (3)
        n4 = Node (4)
        n5 = Node(5)
        #n6 = Node(6)
        n7 = Node(7)
        n1.SetLeft(n2)
        n1.SetRight(n3)
        n2.SetLeft(n4)
        n2.SetRight(n5)
        #n3.SetLeft(n6)
        n3.SetRight(n7)
        MapSiblings(n1, 1, dict())
        PrintTree(n1)

    def test_FullTreeUsingMapSiblings(self):
        print("test_FullTreeUsingMapSiblings")
        n1 = Node (1)    
        n2 = Node (2)
        n3 = Node (3)
        n4 = Node (4)
        n5 = Node(5)
        n6 = Node(6)
        n7 = Node(7)
        n1.SetLeft(n2)
        n1.SetRight(n3)
        n2.SetLeft(n4)
        n2.SetRight(n5)
        n3.SetLeft(n6)
        n3.SetRight(n7)
        MapSiblings(n1, 1, dict())
        PrintTree(n1) 

    def test_OnlyLeftTreeUsingConnect(self):
            print("test_OnlyLeftTreeUsingConnect")
            n1 = Node (1)    
            n2 = Node (2)
            #n3 = Node (3)
            n4 = Node (4)
            #n5 = Node(5)
            #n6 = Node(6)
            #n7 = Node(7)
            n1.SetLeft(n2)
            #n1.SetRight(n3)
            n2.SetLeft(n4)
            #n2.SetRight(n5)
            #n3.SetLeft(n6)
            #n3.SetRight(n7)
            MapSiblings(n1, 1, dict())
            PrintTree(n1)

    def test_OnlyLeftTreeUsingMapSiblings(self):
            print("test_OnlyLeftTreeUsingMapSiblings")
            n1 = Node (1)    
            n2 = Node (2)
            #n3 = Node (3)
            n4 = Node (4)
            #n5 = Node(5)
            #n6 = Node(6)
            #n7 = Node(7)
            n1.SetLeft(n2)
            #n1.SetRight(n3)
            n2.SetLeft(n4)
            #n2.SetRight(n5)
            #n3.SetLeft(n6)
            #n3.SetRight(n7)
            Connect(n1)
            PrintTree(n1)


if __name__ == '__main__':    
    unittest.main()