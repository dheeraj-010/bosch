class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Empty")
            return None
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            print("Empty")
            return None
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(f"Dequeued: {queue.dequeue()}")
print(f"Front item: {queue.peek()}")
print(f"Queue size: {queue.size()}")
