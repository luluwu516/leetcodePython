from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(node, count):
            if not node:
                return False
            if not node.left and not node.right and node.val + count == targetSum:
                return True

            left = helper(node.left, node.val + count)
            right = helper(node.right, node.val + count)

            return left or right

        return helper(root, 0)


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
    print(
        "Enter the values to construct the binary tree (separated by spaces, enter -1 for null nodes)"
    )
    nums = input("> ").split()
    nums = [int(n) for n in nums]

    targetSum = int(input("Enter the target sum: "))

    root = constructBinaryTree(nums)

    # processing
    res = s.hasPathSum(root, targetSum)

    # output
    print("\nResult:")
    print(
        "The root-to-leaf path with the target sum is",
        format("shown" if res else "not shown", "s"),
    )


if __name__ == "__main__":
    main()
