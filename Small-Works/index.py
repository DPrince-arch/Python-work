class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class LinkedLists:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        current = self.head
        element = []
        while current:
            element.append(current.data)
            current = current.next
        
        list_string = " -> ".join(element) + " -> None" if element else "None"
        print(list_string)

def main():
    myList = LinkedLists()
    myList.push(10)
    myList.push(8)
    myList.push(6)

    print("Linked List: ", end="")

main()