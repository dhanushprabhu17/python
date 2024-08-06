#top_down
'''memo=[None]*100
counter=0
def fib(n):
    global counter
    counter+=1
    if memo[n] is not None:
        return memo[n]
    if n==0 or n==1:
        return n
    memo[n]=fib(n-1)+fib(n-2)
    return memo[n]'''

#bottom up
counter=0
def fib(n):
    fib_list=[1,2]
    global counter
    for index in range(2,n+1):
        counter+=1
        next_fib=fib_list[index-1]+fib_list[index-2]
        fib_list.append(next_fib)
    return fib_list[n]

n=35
print('fib of',n,fib(n))
print('Counter:',counter)
    