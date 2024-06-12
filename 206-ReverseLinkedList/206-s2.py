from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        rHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return rHead


def constructLinkList(nums: List[int]) -> Optional[ListNode]:
    if nums == None:
        return None
    head = ListNode(nums[0])
    curr = head
    for i in range(1, len(nums)):
        curr.next = ListNode(nums[i])
        curr = curr.next

    return head


def printList(head: Optional[ListNode]) -> None:
    curr = head
    while curr:
        print(f"{curr.val} ", end="")
        curr = curr.next
    print()


def main():
    # declaration
    s = Solution()

    # input
    nums = input(
        "Enter numbers to construct the Linked List (separated by spaces): "
    ).split()
    nums = [int(n) for n in nums]

    head = constructLinkList(nums)

    # processing and output
    print("\nResult:")
    print("Original: ", end="")
    printList(head)
    res = s.reverseList(head)
    print("Revised : ", end="")
    printList(res)


if __name__ == "__main__":
    main()
