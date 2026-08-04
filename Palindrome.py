class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def palindrome(head):
    slow, fast= head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    prev = None
    current = slow
    while current is not None:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp

    first_half = head
    second_half = prev
    while second_half is not None:
        if first_half.value != second_half.value:
            return False
        first_half = first_half.next
        second_half = second_half.next

    return True
        

def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print("Linked list has palindrome: " + str(palindrome(head)))

main()