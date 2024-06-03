class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    
    
    def swap_first_last(self):
        if self.head is None or self.head == self.tail:
            return
        self.head.value, self.tail.value = self.tail.value, self.head.value
        
        
    
    
    
    def reverse(self):
        if self.length==0:
            return None
        if self.length==1:
            return self.print_list()
        
        current_node=self.head
        while current_node is not None:
            
            current_node.next,current_node.prev=current_node.prev,current_node.next
            current_node=current_node.prev
            
        self.head,self.tail=self.tail,self.head
        
        
        
    def is_palindrome(self):
        if self.length==0:
            return True
        if self.length==1:
            return True
        temp_forward=self.head
        temp_backward=self.tail
        while temp_backward is not None:
            if temp_backward.value != temp_forward.value:
                return False
            temp_forward=temp_forward.next
            temp_backward=temp_backward.prev
        return True
    
    
    
    def swap_pairs(self):
        dummy_node = Node(0)
        dummy_node.next = self.head
        previous_node = dummy_node
    
        while self.head and self.head.next:
            first_node = self.head
            second_node = self.head.next
    
            previous_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
    
            second_node.prev = previous_node
            first_node.prev = second_node
    
            if first_node.next:
                first_node.next.prev = first_node
    
            self.head = first_node.next
            previous_node = first_node
    
        self.head = dummy_node.next
    
        if self.head:
            self.head.prev = None
        
        