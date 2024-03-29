from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1


def constructBinaryTree(nums: list):
    if len(nums) == 0 or nums[0] == -1:
        return None

    tree_nodes = []
    for i in range(len(nums)):
        if nums[i] != -1:
            tree_nodes.append(TreeNode(nums[i]))
        else:
            tree_nodes.append(None)

    # print("\ntree_nodes: ")
    # for t in tree_nodes:
    #     if t != None:
    #         print(t.val)

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

    root = constructBinaryTree(nums)

    # processing
    res = s.maxDepth(root)

    # output
    print("\nResult:")
    print(f"The depth of the tree is {res}")


if __name__ == "__main__":
    main()
