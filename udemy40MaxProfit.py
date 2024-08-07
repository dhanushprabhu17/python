#You are given a list of integers representing stock prices for a certain company over a period of time, where each element in the list corresponds to the stock price for a specific day
def min_index(prices):
    min_index=0
    for i in range(len(prices)):
        if prices[i]<prices[min_index]:
             min_index=i
    return min_index

def max_profit(prices):
    min_indexx=min_index(prices)
    if min_indexx==len(prices):
        prices.pop(min_indexx)
        min_indexx=min_indexx(prices)
    max_val=0
    for i in range(min_indexx,len(prices)):
        if prices[i]>max_val:
            max_val=prices[i]
    return (max_val-prices[min_indexx])

