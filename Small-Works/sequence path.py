class TreeNodde:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def path_sequence(root, sequence):
    if not root:
        return len(sequence) == 0

    return find_path_recursive(root, sequence, 0)

def find_path_recursive(current_node, sequence, sequence_index):
    if not current_node:
        return False

    if sequence_index >= len(sequence) or current_node.val != sequence[sequence_index]:
        return False

    if not current_node.left and not current_node.right and sequence_index == len(sequence) - 1:
        return True

    return (find_path_recursive(current_node.left, sequence, sequence_index + 1) or
            find_path_recursive(current_node.right, sequence, sequence_index + 1))

def main():
    root = TreeNodde(1)
    root.left = TreeNodde(0)
    root.right = TreeNodde(1)
    root.left.left = TreeNodde(1)
    root.right.left = TreeNodde(6)
    root.right.right = TreeNodde(5)

    print("Path sequence [1, 0, 7] exists: " + str(path_sequence(root, [1, 0, 7])))
    print("Path sequence [1, 1, 6] exists: " + str(path_sequence(root, [1, 1, 6])))

if __name__ == "__main__":
    main()