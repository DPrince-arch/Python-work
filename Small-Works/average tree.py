from collections import deque

class Treenode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def traverse(self):
    result = []
    queue = deque()
    queue.append(self)
    
    while queue:
        size = len(queue)
        level = []
        for _ in range(size):
            current_node = queue.popleft()
            level.append(current_node.value)        

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
                  
        result.append(level)
        total = 0
        for i in level:
            total += i
        average = total / len(level)
        result.append(average)


    return list(result)
    
def main():
    root = Treenode(1)
    root.left = Treenode(2)
    root.right = Treenode(3)
    root.left.left = Treenode(4)
    root.left.right = Treenode(5)
    root.right.left = Treenode(6)
    root.right.right = Treenode(7)

    print("Average values of each level in the binary tree:", traverse(root))

main()