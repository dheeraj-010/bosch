class Node:
    def __init__(self, new_data):

        self.data = new_data
        self.next = None


def reverseList(head):

    stack = []
    temp = head
    while temp.next is not None:
        stack.append(temp)
        temp = temp.next

    head = temp
    while stack:
        temp.next = stack.pop()
        temp = temp.next

    temp.next = None
    return head


def printList(node):
    while node is not None:
        print(f"{node.data}", end="")
        if node.next is not None:
            print(" -> ", end="")
        node = node.next
    print(" -> NULL")

if __name__ == "__main__":
  
    head=Node(1)
    b=Node(2)
    c=Node(3)
    d=Node(4)
    e=Node(5)

    head.next=b
    b.next=c
    c.next=d
    d.next=e

    print("before reversal :")
    printList(head)
    head = reverseList(head)
    print("after reversal :")
    printList(head)