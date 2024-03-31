from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not len(nums):
            return None
        elif len(nums) == 1:
            return TreeNode(nums[0])
        else:
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = self.sortedArrayToBST(nums[0:mid])
            root.right = self.sortedArrayToBST(nums[mid + 1 : len(nums)])
            return root


def printTree(root: TreeNode):
    if not root:
        print("Tree is empty")
        return

    def nodeValue(node: TreeNode):
        if not node:
            return None
        return node.val

    def printHelper(node: TreeNode):
        if not node:
            return []

        queue = [node]
        result = []

        while queue and queue[-1] != None:
            level_size = len(queue)
            level_nodes = []

            for _ in range(level_size):
                current = queue.pop(0)
                level_nodes.append(nodeValue(current))

                if current:
                    queue.append(current.left)
                    queue.append(current.right)

            result.extend(level_nodes)

        return result

    nodes = printHelper(root)
    print(nodes)


def main():
    # declaration
    s = Solution()

    # input
    nums = input("Enter the values (separated by comma): ").split(",")
    nums = [int(n) for n in nums]
    nums.sort()

    # processing
    res = s.sortedArrayToBST(nums)

    # output
    print("\nResult:")
    printTree(res)


if __name__ == "__main__":
    main()
