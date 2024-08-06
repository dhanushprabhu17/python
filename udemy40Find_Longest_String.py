#Write a Python function called find_longest_string that takes a list of strings as an input and returns the longest string in the list. The function should iterate through each string in the list, check its length, and keep track of the longest string seen so far. Once it has looped through all the strings, the function should return the longest string found
def find_longest_string(string_list):
    max_string=''
    if len(string_list)==0:
        return ''
    for i in range(len(string_list)):
        if len(string_list[i])>len(max_string):
            max_string=string_list[i]
    return max_string