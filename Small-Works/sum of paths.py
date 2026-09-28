class TreeNodde:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_of_path_numbers(root):
    if not root:
        return 0

    total_sum = 0
    stack = [(root, root.val)]

    while stack:
        current_node, current_sum = stack.pop()

        if not current_node.left and not current_node.right:
            total_sum += current_sum

        if current_node.right:
            stack.append((current_node.right, current_sum * 10 + current_node.right.val))
        if current_node.left:
            stack.append((current_node.left, current_sum * 10 + current_node.left.val))

    return total_sum

def main():
    root = TreeNodde(1)
    root.left = TreeNodde(2)
    root.right = TreeNodde(3)
    root.left.left = TreeNodde(4)
    root.left.right = TreeNodde(5)
    root.right.left = TreeNodde(6)
    root.right.right = TreeNodde(7)

    print("Total sum of all path numbers: " + str(sum_of_path_numbers(root)))

if __name__ == "__main__":  
    main()