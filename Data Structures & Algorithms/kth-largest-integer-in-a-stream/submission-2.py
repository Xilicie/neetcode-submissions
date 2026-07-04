class KthLargest:
    minHeap = 0
    k = 0
    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > self.k:   
        # we pop elements until the size of our heap is k long
            heapq.heappop(self.minHeap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        kLargest = heapq.heappop(self.minHeap)
        heapq.heappush(self.minHeap, kLargest)
        return kLargest
            
        



