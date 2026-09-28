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

    def rotateList(self, k):
        if not self:
            return None

        last_node = self
        length = 1
        while last_node.next:
            last_node = last_node.next
            length += 1

        last_node.next = self

        k = k % length
        new_tail = self
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        return new_head
    
def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    print("Original list: ", end="")
    head.printNode()

    k = 3
    rotated_head = head.rotateList(k)

    print(f"Rotated list by {k} positions: ", end="")
    rotated_head.printNode()
 
main()