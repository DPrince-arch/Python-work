from __future__ import print_function

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def printNode(self):
        temp = self
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()

def reverse(head):
    prev = None
    current = head

    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)

    print("Original list: ", end="")
    head.printNode()

    reversed_head = reverse(head)

    print("Reversed list: ", end="")
    reversed_head.printNode()

main()