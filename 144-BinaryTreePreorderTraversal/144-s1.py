from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.helper(root, res)
        return res

    def helper(self, root: Optional[TreeNode], res: list):
        if root != None:
            res.append(root.val)
            self.helper(root.left, res)
            self.helper(root.right, res)

    # def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     res = []

    #     def helper(root):
    #         if root == None:
    #             return
    #         l.append(root.val)
    #         helper(root.left)
    #         helper(root.right)

    #     helper(root)
    #     return res


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
    nums = input(
        "Enter the values to construct the binary tree (separated by spaces, enter -1 for null nodes): "
    ).split()
    nums = [int(n) for n in nums]

    root = constructBinaryTree(nums)

    # processing
    res = s.preorderTraversal(root)

    # output
    print("\nPreorder Traversal Result:", res)


if __name__ == "__main__":
    main()
