class TreeNodde:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_paths(root, target_sum):
    if not root:
        return 0

    path_count = {0: 1}
    return count_paths_recursive(root, target_sum, 0, path_count)   

def count_paths_recursive(current_node, target_sum, current_path_sum, path_count):
    if not current_node:
        return 0

    current_path_sum += current_node.val
    sum_needed = current_path_sum - target_sum
    total_paths = path_count.get(sum_needed, 0)

    path_count[current_path_sum] = path_count.get(current_path_sum, 0) + 1

    total_paths += count_paths_recursive(current_node.left, target_sum, current_path_sum, path_count)
    total_paths += count_paths_recursive(current_node.right, target_sum, current_path_sum, path_count)

    path_count[current_path_sum] -= 1

    return total_paths

def main():
    root = TreeNodde(12)
    root.left = TreeNodde(7)
    root.right = TreeNodde(1)
    root.left.left = TreeNodde(4)
    root.right.left = TreeNodde(10)
    root.right.right = TreeNodde(5)

    target_sum = 11
    print("Count of paths with sum " + str(target_sum) + ": " + str(count_paths(root, target_sum)))

if __name__ == "__main__":
    main()