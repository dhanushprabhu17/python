def stream_max(nums):
    my_heap=MaxHeap()
    max_stream=[]
    for i in nums:
        my_heap.insert(i)
        max_stream.append(my_heap.heap[0])
    return max_stream