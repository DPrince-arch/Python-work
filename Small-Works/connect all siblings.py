from collections import deque

class Treenode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next = None 

    def print_tree(self):
        print("Traversal using 'next' pointers: ")
        current = self
        while current:
            print(str(current.value) + " ", end='')
            current = current.next

def connect_all_siblings(root):
    if not root:
        return None

    queue = deque([root])
   
    current_node, prev = None, None
    while queue:        
        current_node = queue.popleft()
        if prev:
            prev.next = current_node
        prev = current_node

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)


def main():
    root = Treenode(1)
    root.left = Treenode(2)
    root.right = Treenode(3)
    root.left.left = Treenode(4)
    root.left.right = Treenode(5)
    root.right.left = Treenode(6)
    root.right.right = Treenode(7)
    connect_all_siblings(root)

    root.print_tree()


main()