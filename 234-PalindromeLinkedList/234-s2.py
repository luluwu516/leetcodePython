from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        stack = []
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next

        # curr = head
        # while stack:
        #     if stack.pop() != curr.val:
        #         return False
        #     curr = curr.next

        # return True

        curr = head
        last = len(stack) - 1
        half = len(stack) // 2

        while last >= half:
            if stack[last] != curr.val:
                return False
            curr = curr.next
            last -= 1

        return True


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
