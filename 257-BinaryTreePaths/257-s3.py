from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res, queue = list(), list()
        if root is None:
            return res
        queue.append([root, ""])

        while queue:
            node, path = queue.pop(0)
            if node is None:
                continue
            path += f"{node.val}->"
            if node.left is None and node.right is None:
                res.append(path[:-2])
                continue
            queue.append([node.left, path])
            queue.append([node.right, path])

        return res

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def helper(node):
            if node == None:
                return
            res.append(node.val)
            helper(node.left)
            helper(node.right)

        helper(root)
        return res


def constructBinaryTree(nums: list) -> Optional[TreeNode]:
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
    original = s.preorderTraversal(root)

    # processing
    res = s.binaryTreePaths(root)

    # output
    print("\nOriginal: ")
    for val in original:
        print(val, end=" ")
    print()
    print("Result: ")
    for val in res:
        print(val, end=" ")
    print()


if __name__ == "__main__":
    main()
