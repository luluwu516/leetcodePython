from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False


def constructLinkedList(nums: list, pos: int) -> ListNode:
    if not nums:
        return None

    nodes = []
    for n in nums:
        nodes.append(ListNode(n))

    for i in range(len(nums) - 1):
        nodes[i].next = nodes[i + 1]

    if pos >= 0 and pos < len(nums):
        nodes[len(nums) - 1].next = nodes[pos]

    return nodes[0]


def main():
    # declaration
    s = Solution()

    # input
    nums = input("Enter the prices (separated by comma): ").split(",")
    nums = [int(n) for n in nums]
    pos = int(
        input(
            "Enter the connected position or -1 to create a linked list without a cycle: "
        )
    )

    head = constructLinkedList(nums, pos)

    # processing
    res = s.hasCycle(head)

    # output
    print("\nResult:")
    print("The linked list", (" has" if res else " doesn't have"), " a cycle", sep="")


if __name__ == "__main__":
    main()
