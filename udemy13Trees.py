#constructor
class Node:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None
        
        
class BinarySearchTree:
    def __init__(self):
        #new_node=Node(value)
        #self.root=new_node
        self.root=None
        
        #initially create node pointing to none
        
    def insert(self,value):
        new_node=Node(value)
        if self.root is None:
            self.root=new_node
            return True
        temp=self.root
        while(True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left=new_node
                    return True
                temp=temp.left
            else:
                if temp.right is None:
                    temp.right=new_node
                    return True
                temp=temp.right
                
                
                
    def contains(self,value):
        '''if self.root is None:
            return False'''
        temp=self.root
        while temp is not None:
            if value< temp.value:
                temp=temp.left
            elif value>temp.value:
                temp=temp.right
            else:
                return True
        return False
    
    
    
    def __r_contains(self,current_node,value):
        if current_node==None:
            return False
        if current_node.value==value:
            return True
        if current_node.value>value:
            return self.__r_contains(current_node.left,value)
        if current_node.value<value:
            return self.__r_contains(current_node.right,value)
        
    def r_contains(self,value):
        return self.__r_contains(self.root,value)
    
    
    def __r_insert(self,current_node,value):
        if current_node==Node:
            return Node(value)
        if value<current_node.value:
            current_node.left=self.__r_contains(current_node.left,value)
        if value>current_node.value:
            current_node.right=self.__r_contains(current_node.right,value)
        return current_node
    
    def r_insert(self,value):
        if self.root==None:
            self.root=Node(value)
        self.__r_insert(self.root,value)
        
    def min_value(self,current_node):
        while current_node.left is not None:
            current_node=current_node.left
        return current_node.value
    def __delete_node(self,current_node,value):
        if current_node==None:
            return None
        if value<current_node.value:
            current_node.left=self.__delete_node(current_node.left,value)
        elif value>current_node.value:
            current_node.right=self.__delete_node(current_node.right,value)
        else:
            if current_node.left==None and current_node.right==None:
                return None
            elif current_node.left==None:
                current_node=current_node.right
            elif current_node.right==None:
                current_node=current_node.left
            else:
                sub_tree_min=self.min_value(current_node.right)
                current_node.value=sub_tree_min
                current_node.right=self.__delete_node(current_node.right,sub_tree_min)
        return current_node
    
    def delete_node(self,value):
        self.__delete_node(self.root,value)
            
    
            
        
my_tree=BinarySearchTree()
'''my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

#print(my_tree.r_contains(27))
#print(my_tree.r_contains(17))
#print(my_tree.root.value)
#print(my_tree.root.left.value)
#print(my_tree.root.right.value)
               
print(my_tree.min_value(my_tree.root))
print(my_tree.min_value(my_tree.root.right ))'''

my_tree.r_insert(2)
my_tree.insert(1)
my_tree.insert(3)

print("root",my_tree.root.value)
print("root.left=",my_tree.root.left.value)
print("root.right=",my_tree.root.right.value)

my_tree.delete_node(2)

print("root",my_tree.root.value)
print("root.left=",my_tree.root.left.value)
print("root.right=",my_tree.root.right.value)