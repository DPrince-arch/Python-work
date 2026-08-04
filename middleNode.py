class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def findMiddleNode(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    return slow.value

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    
    print("Linked list middle node: " + str(findMiddleNode(head)))
    print("Linked list middle node: " + str(findMiddleNode(head)))
    print("Linked list middle node: " + str(findMiddleNode(head)))


main()