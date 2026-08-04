from __future__ import print_function

class Node:
    def __init__(self, value, next=None):
        self. value = value
        self.next = next

    def printList(self):
        temp = self
        while temp is not None:
            print(temp.value, end='')
            temp = temp.next
        print()

    def findHead():
        ...
    
def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print("Linked list has cycle: " + str(Node.hasCycle(head)))

    head.next.next.next.next.next.next = head.next.next
    print("Linked list has cycle: " + str(Node.hasCycle(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("Linked list has cycle: " + str(Node.hasCycle(head)))

main()