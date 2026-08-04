class TreeNodde:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def has_path_sum(root, target_sum):
    if not root:
        return False

    if not root.left and not root.right:
        return target_sum == root.val

    target_sum -= root.val
    return has_path_sum(root.left, target_sum) or has_path_sum(root.right, target_sum)

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
    print("Path with sum " + str(target_sum) + ": " + str(has_path_sum(root, target_sum)))

if __name__ == "__main__":
    main()