class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


    def PQInsert(self, item):
        
        self.items.append(item)
        length = len(self.items)
        self.orderHeap(0, length)

    def orderHeap(self, i, n):
        PQ = self.items
        if(((2 * i) < n) and (PQ[2*i].goalDistance < PQ[i].goalDistance)):
            smallest = 2*i
        else:
            smallest=i
        if ((((2*i)+1) < n) and (PQ[2*i+1].goalDistance < PQ[smallest].goalDistance)):
            smallest=(2*i)+1
        
        if (smallest != i):
            x = PQ[i]
            PQ[i] = PQ[smallest]
            PQ[smallest] = x
            self.items = PQ
            self.orderHeap(smallest,n)
        else:
            self.items = PQ

    def removeMin(self):
        PQ = self.items
        length = len(PQ)
        min = PQ[0]
        
        PQ[0] = PQ[length - 1]
        length -= 1
        PQ.pop()
        self.items = PQ
        if(length > 0):
            self.orderHeap(0, length)
        return min