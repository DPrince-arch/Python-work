from heapq import *

class Median:

    maxHeap = []
    minHeap = []

    def insertNum(self, num):
        if not self.maxHeap or -self.maxHeap[0] >= 0:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))

    def findMedian(self):
        if len(self.maxHeap) == len(self.minHeap):
            return self.maxHeap[0] / 2 + self.minHeap[0] / 2
        else:
            return self.maxHeap[0] / 1

def main():
    streamMedian = Median()
    streamMedian.insertNum(4)
    streamMedian.insertNum(2)
    print("The median of the stream is " + str(streamMedian.findMedian()))

main()