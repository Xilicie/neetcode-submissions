class MedianFinder:

    def __init__(self):
        self.left = []  # maxheap
        self.right = [] # minheap
        # len(left) == len(right)
        # lenNums == len(left) + len(right)

    def addNum(self, num: int) -> None:
        if not self.left:
            heapq.heappush(self.left, -num)
        elif len(self.left) == len(self.right):
            if num > self.right[0]:
                heapq.heappush(self.right, num)
                heapq.heappush(self.left, -heapq.heappop(self.right))
            else:
                heapq.heappush(self.left, -num)
        else:
            if num < -self.left[0]:
                heapq.heappush(self.left, -num)
                heapq.heappush(self.right, -heapq.heappop(self.left))
            else:
                heapq.heappush(self.right, num)
            

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        else:
            return float(-self.left[0])
        