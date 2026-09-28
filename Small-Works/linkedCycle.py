class Node:
    def __init__(self, value, next=None):
        self. value = value
        self.next = next

    def hasCycle(head):
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
            else:
                return False
    
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