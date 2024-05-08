from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []

        curr = root
        lastVisited = None
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                temp = stack[-1]
                if temp.right and temp.right != lastVisited:
                    curr = temp.right
                else:
                    stack.pop()
                    res.append(temp.val)
                    lastVisited = temp
        return res


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
    res = s.postorderTraversal(root)

    # output
    print("\nPreorder Traversal Result:", res)


if __name__ == "__main__":
    main()
