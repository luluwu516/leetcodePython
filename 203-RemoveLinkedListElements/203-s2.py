from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return dummy.next


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
    num = int(input("Enter a value to remove: "))

    head = constructLinkList(nums)

    # processing and output
    print("\nResult:")
    print("Original: ", end="")
    printList(head)
    res = s.removeElements(head, num)
    print("Revised : ", end="")
    printList(res)


if __name__ == "__main__":
    main()
