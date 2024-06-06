class Stack:
    def __init__(self):
        self.stack_list=[]
        
    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])


    def push(self,value):
        #self.stack_list.append(value)
        self.stack_list+=[value]
        
    def is_empty(self):
        return len(self.stack_list) == 0
    
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)
    
    def pop(self):
        if self.is_empty():
            return None
        return self.stack_list.pop()
    
    
    def is_balanced_parentheses(lis):
    stack=Stack()
    for i in lis:
        if i=="(":
            stack.push("(")
        elif i==")":
        
            if stack.is_empty() or stack.pop()!="(":
                return False
    return stack.is_empty() 


def reverse_string(string):
    stack = Stack()
    reversed_string = ""
 
    for char in string:
        stack.push(char)
 
    while not stack.is_empty():
        reversed_string += stack.pop()
 
    return reversed_string

def sort_stack(stack):
    additional_stack = Stack()
 
    while not stack.is_empty():
        temp = stack.pop()
 
        while not additional_stack.is_empty() and additional_stack.peek() > temp:
            stack.push(additional_stack.pop())
 
        additional_stack.push(temp)
 
    while not additional_stack.is_empty():
        stack.push(additional_stack.pop())
        
        
        
def enqueue(self,value):
        for i in self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(value)
        for i in self.stack2:
            self.stack1.append(self.stack2.pop())
        return self.stack1
    
    
    def dequeue(self): 
    
        if len(self.stack1)==0:
            return None
        return self.stack1.pop()

        