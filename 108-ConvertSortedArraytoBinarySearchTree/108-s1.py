from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            root = TreeNode(nums[mid])
            root.left = helper(l, mid - 1)
            root.right = helper(mid + 1, r)
            return root

        return helper(0, len(nums) - 1)


def printTree(root: TreeNode):
    if not root:
        print("Tree is empty")
        return

    def height(node: TreeNode) -> int:
        if not node:
            return 0
        return 1 + max(height(node.left), height(node.right))

    def printLevel(node: TreeNode, level: int):
        if not node:
            return
        if level == 1:
            print(node.val, end=" ")
        elif level > 1:
            printLevel(node.left, level - 1)
            printLevel(node.right, level - 1)

    h = height(root)
    for i in range(1, h + 1):
        print("Level ", i, ":", sep="", end=" ")
        printLevel(root, i)
        print()


# def printTree(root: TreeNode):
#     if not root:
#         print("Tree is empty")
#         return

#     def printNode(node: TreeNode):
#         if not node:
#             return "null"
#         return str(node.val)

#     def printHelper(node: TreeNode):
#         if not node:
#             return []

#         queue = [node]
#         result = []

#         while queue:
#             level_size = len(queue)
#             level_nodes = []

#             for _ in range(level_size):
#                 current = queue.pop(0)
#                 level_nodes.append(printNode(current))

#                 if current:
#                     queue.append(current.left)
#                     queue.append(current.right)

#             result.extend(level_nodes)

#         return result

#     nodes = printHelper(root)
#     print("Output:")
#     print(nodes)


def main():
    # declaration
    s = Solution()

    # input
    nums = input("Enter the values (separated by spaces): ").split()
    nums = [int(n) for n in nums]

    # processing
    res = s.sortedArrayToBST(nums)

    # output
    print("\nResult:")
    printTree(res)


if __name__ == "__main__":
    main()
