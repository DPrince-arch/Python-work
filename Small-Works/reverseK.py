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

    def reverseK(self, k):
        prev = None
        current = self
        next = None
        count = 0

        while current and count < k:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1

        if next:
            self.next = next.reverseK(k)

        return prev
    
def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Original list: ", end="")
    head.printNode()

    k = 2
    reversed_head = head.reverseK(k)

    print(f"Reversed list in groups of {k}: ", end="")
    reversed_head.printNode()

main()