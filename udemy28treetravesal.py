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


    def BFS(self):
        current_node=self.root
        results=[]
        queue=[]
        queue.append(current_node)
        while len(queue)>0:
            current_node=queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results
    
    def dfs_pre_order(self):
        results=[]
        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results
    
    def dfs_post_order(self):
        results=[]
        def traverse(current_node):
            
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)
        traverse(self.root)
        return results
    
    def dfs_in_order(self):
        results=[]
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results
    
my_tree=BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.dfs_post_order())
