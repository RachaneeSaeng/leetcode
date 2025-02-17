class CustomHeap:
    def __init__(self):
        self.heap = []

    def heappush(self, item):
        self.heap.append(item)
        self._siftup(len(self.heap) - 1)

    def heappop(self):
        if len(self.heap) == 0:
            raise IndexError("pop from empty heap")
        lastelt = self.heap.pop() # the last element in the heap array
        if self.heap:
            returnitem = self.heap[0]
            self.heap[0] = lastelt
            self._siftdown(0)
            return returnitem
        return lastelt

    def heapreplace(self, item):
        if len(self.heap) == 0:
            raise IndexError("replace from empty heap")
        returnitem = self.heap[0]
        self.heap[0] = item
        self._siftdown(0)
        return returnitem

    def _siftup(self, pos):
        newitem = self.heap[pos]
        while pos > 0:
            parentpos = (pos - 1) >> 1 ## hifting a number to the right by one bit, equivalent to performing integer division by 2.
            parent = self.heap[parentpos]
            if newitem < parent:
                self.heap[pos] = parent
                pos = parentpos
                continue
            break
        self.heap[pos] = newitem

    def _siftdown(self, pos):
        endpos = len(self.heap)
        startpos = pos
        newitem = self.heap[pos]
        childpos = 2 * pos + 1
        while childpos < endpos:
            rightpos = childpos + 1
            if rightpos < endpos and not self.heap[childpos] < self.heap[rightpos]:
                childpos = rightpos
            self.heap[pos] = self.heap[childpos]
            pos = childpos
            childpos = 2 * pos + 1
        self.heap[pos] = newitem
        self._siftup(pos)