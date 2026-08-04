class TreeNodde:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def find_all_paths(root, target_sum):
    all_paths = []
    find_paths_recursive(root, target_sum, [], all_paths)
    return all_paths

def find_paths_recursive(root, target_sum, current_path, all_paths):
    if not root:
        return

    current_path.append(root.val)

    if not root.left and not root.right and target_sum == root.val:
        all_paths.append(list(current_path))
    else:
        find_paths_recursive(root.left, target_sum - root.val, current_path, all_paths)
        find_paths_recursive(root.right, target_sum - root.val, current_path, all_paths)

    current_path.pop()

def main():
    root = TreeNodde(5)
    root.left = TreeNodde(4)
    root.right = TreeNodde(8)
    root.left.left = TreeNodde(11)
    root.right.left = TreeNodde(13)
    root.right.right = TreeNodde(4)
    root.left.left.left = TreeNodde(7)
    root.left.left.right = TreeNodde(2)
    root.right.right.right = TreeNodde(1)

    target_sum = 22
    print("All paths with sum " + str(target_sum) + ": " + str(find_all_paths(root, target_sum)))

if __name__ == "__main__":
    main()