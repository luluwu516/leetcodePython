from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def depth(root) -> int:
            count = 0
            while root:
                count += 1
                root = root.left
            return count

        if not root:
            return 0
        dl = depth(root.left)
        dr = depth(root.right)
        if dl == dr:
            return 1 + (2**dl - 1) + self.countNodes(root.right)
        else:
            return 1 + self.countNodes(root.left) + (2**dr - 1)


def constructBinaryTree(nums: list):
    if len(nums) == 0 or nums[0] == -1:
        return None

    tree_nodes = []
    for i in range(len(nums)):
        if nums[i] != -1:
            tree_nodes.append(TreeNode(nums[i]))
        else:
            tree_nodes.append(None)

    leftIndex = 1
    rightIndex = 2
    for i in range(len(nums)):
        if tree_nodes[i] != None:
            if leftIndex < len(nums):
                tree_nodes[i].left = tree_nodes[leftIndex]
            if rightIndex < len(nums):
                tree_nodes[i].right = tree_nodes[rightIndex]
            leftIndex += 2
            rightIndex += 2

    return tree_nodes[0]


def main():
    # declaration
    s = Solution()

    # input
    nums = input("Enter numbers (separated by spaces) to construct the tree: ").split()
    nums = [int(n) for n in nums]

    root1 = constructBinaryTree(nums)

    # processing
    res = s.countNodes(root1)

    # output
    print(f"\nThere are {res} nodes in the tree.")


if __name__ == "__main__":
    main()
