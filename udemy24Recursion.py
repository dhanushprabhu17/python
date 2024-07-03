def funcThree():
    print("three")
    
def funcTwo():
    funcThree()
    print("two")
    
def funcOne():
    funcTwo()
    print("One")
    
    
funcOne()