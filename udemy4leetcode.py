class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
        

    
    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    # WRITE FIND_MIDDLE_NODE METHOD HERE #
    #                                    #
    #                                    #
    #                                    #
    #                                    #
    ######################################




my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)




def has_loop(self):
        slow=self.head
        fast=self.head
        while fast is not None and fast.next is not None :
            fast=fast.next.next
            slow=slow.next
            if slow==fast:
                return True
        return False
    
    
def find_kth_from_end(ll,k):
    fast=ll.head
    
    slow=ll.head
    for i in range(k):
        
        if fast is None:
            return None
        fast=fast.next
      
    while fast is not None:
        fast=fast.next
        slow=slow.next
    return slow
    
    
    
def remove_duplicates(self):
        previous=None
        current=self.head
        values=set()
        while current:
            if current.value in values:
                previous.next=current.next
                
                
                
            else:
                values.add(current.value)
                previous=current
            current=current.next
            
            


def binary_to_decimal(self):
        num = 0
        current = self.head
        while current:
            num = num * 2 + current.value
            current = current.next
        return num