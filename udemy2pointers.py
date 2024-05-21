"""num1=11
num2=num1

print('before num2 value is updated:')
print('num1=',num1)
print('num2=',num2)

print("\nnum1 points to:",id(num1))
print("num2 points to:",id(num2))

num2=22

print("\nAfte num2 value is updated:")
print('num1=',num1)
print('num2=',num2)

print("\nnum1 points to:",id(num1))
print("num2 points to:",id(num2))"""

dict1={ 'value':11}
dict2= dict1

print(dict1)
print(dict2)

print(id(dict1))
print(id(dict2))

dict2['value']=22

print(dict1)
print(dict2)

print(id(dict1))
print(id(dict2))



