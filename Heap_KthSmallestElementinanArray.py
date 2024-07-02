def find_kth_smallest(nums,k):
    max_heap=MaxHeap()
    for i in nums:
        max_heap.insert(i)
        if len(max_heap.heap)>k:
            max_heap.remove()
            
    return max_heap.remove()