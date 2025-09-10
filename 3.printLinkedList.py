class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next
def printLinkedList(head):
    current = head
    while current:
        print(current.data)
        current = current.next
    print()


head = Node(1)
second = Node(2)
third = Node(3)

head.next = second
second.next = third


print("Linked List:")
printLinkedList(head)