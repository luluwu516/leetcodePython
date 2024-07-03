from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        reversed_second_half = self.reverseLinkedList(slow.next)
        slow.next = None
        first_half = head
        while reversed_second_half:
            if reversed_second_half.val != first_half.val:
                return False
            first_half = first_half.next
            reversed_second_half = reversed_second_half.next

        return True

    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        rHead = self.reverseLinkedList(head.next)
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

    # processing
    res = s.isPalindrome(head)

    # output
    print("\nResult:")
    print(f"The Linked List, {nums}, is{'' if res else ' not'} palindrome\n")


if __name__ == "__main__":
    main()
