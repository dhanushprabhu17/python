def find_duplicates(nums):
    list_dup=[]
    for i in nums:
        if i not in list_dup:
            ct=0
            for j in nums:
                if j==i:
                    ct+=1
            
            if ct>=2:
                list_dup.append(i)
    return list_dup


#method 2

'''def find_duplicates(nums):
    list_dup=[]
    for i in nums:
        if i not in list_dup:
            ct=nums.count(i)
             """for j in nums:
                if j==i:
                    ct+=1"""
            
            if ct>=2:
                list_dup.append(i)    
                return 
                
                
 #method 3               
                
def find_duplicates(nums):
    num_counts = {}
    for num in nums:
        num_counts[num] = num_counts.get(num, 0) + 1
 
    duplicates = []
    for num, count in num_counts.items():
        if count > 1:
            duplicates.append(num)
 
    return duplicates                '''
                
                
                
    