from collections import deque

class Treenode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_successor(root, key):
    if not root:
        return None

    queue = deque([root])

    while queue:
        current_node = queue.popleft()

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

        if current_node.value == key:
            return queue[0] if queue else None

    return None

def main():
    root = Treenode(1)
    root.left = Treenode(2)
    root.right = Treenode(3)
    root.left.left = Treenode(4)
    root.left.right = Treenode(5)
    root.right.left = Treenode(6)
    root.right.right = Treenode(7)

    result = find_successor(root, 3)
    if result:
        print("Successor of 3 is:", result.value) 
    else:
        print("No successor found.")

main()