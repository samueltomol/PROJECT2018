#Samuel C. Tomol
#github.com/samueltomol
#QUEUE AND DEQUEUE

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        self.items.pop()

    def size(self):
        return len(self.items)

    def printqueue(self):
        for items in self.items:
            print (items)

q = Queue()
print(q.isEmpty())
q.enqueue(200)
q.enqueue(400)
q.enqueue(600)
q.enqueue(800)
q.enqueue(1000)
q.enqueue(1200)
q.printqueue()
q.dequeue()
print("\n")
q.printqueue()
