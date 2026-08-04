from collections import deque

class Treenode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def traverse(root):
    if not root:
        return 0
        
    queue = deque([root])
    depth = 0
    
    while queue:
        depth += 1
        size = len(queue)
        for _ in range(size):
            current_node = queue.popleft()
            
            if not current_node.left and not current_node.right:
                return depth
                
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

    return depth

def main():
    root = Treenode(1)
    root.left = Treenode(2)
    root.right = Treenode(3)
    #root.left.left = Treenode(4)
    #root.left.right = Treenode(5)
    root.right.left = Treenode(6)
    root.right.right = Treenode(7)

    print("Shortest depth of the binary tree:", traverse(root))

main()