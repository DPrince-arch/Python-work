from collections import deque

class Treenode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next = None 

    def print_level_order(self):
        next = self
        while next:
            current = next
            next = None
            while current:
                print(str(current.value) + " ", end='')
                if not next:
                    if current.left:
                        next = current.left
                    elif current.right:
                        next = current.right
                current = current.next
            print()

def connect_siblings(root):
    if not root:
        return None

    queue = deque([root])

    while queue:
        prev = None
        size = len(queue)
        for _ in range(size):
            current_node = queue.popleft()

            if prev:
                prev.next = current_node
            prev = current_node

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

    return 

def main():
    root = Treenode(1)
    root.left = Treenode(2)
    root.right = Treenode(3)
    root.left.left = Treenode(4)
    root.left.right = Treenode(5)
    root.right.left = Treenode(6)
    root.right.right = Treenode(7)
    connect_siblings(root)

    print("Level order traversal using 'next' pointers: ")
    root.print_level_order()


main()