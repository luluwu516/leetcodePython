from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.helper(p, q)

    def helper(self, l: Optional[TreeNode], r: Optional[TreeNode]):
        # if (l is None and r is not None) or (r is None and l is not None):
        #     return False
        if (l is None) and (r is None):
            return True
        if (l is None) or (r is None):
            return False
        if l.val != r.val:
            return False

        return self.helper(l.left, r.left) and self.helper(l.right, r.right)


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
        "Enter the values to construct the binary trees (separated by spaces, enter -1 for null nodes)"
    )
    nums1 = input("The first binary tree : ").split()
    nums1 = [int(n) for n in nums1]

    nums2 = input("The second binary tree: ").split()
    nums2 = [int(n) for n in nums2]

    root1 = constructBinaryTree(nums1)
    root2 = constructBinaryTree(nums2)

    # processing
    res = s.isSameTree(root1, root2)

    # output
    if res:
        print("\nThey are the same tree")
    else:
        print("\nThey are not the same tree")


if __name__ == "__main__":
    main()
