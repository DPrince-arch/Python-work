class Exit:
    def __init__(self, data):
        self.data = data
        self.next = None

def removeRandomValue(head):
    minValue = head.data
    currentNode = head.next
    

node1 = Exit(7)
node2 = Exit(11)
node3 = Exit(3)
node4 = Exit(2)
node5 = Exit(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

#print("The lowest value in the linked list is:", findLowestValue(node1))