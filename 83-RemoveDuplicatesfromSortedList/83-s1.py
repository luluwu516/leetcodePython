from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        prev = head
        curr = prev.next

        while curr != None:
            if prev.val == curr.val:
                curr = curr.next
                prev.next = curr
            else:
                curr = curr.next
                prev = prev.next

        return head


def printList(head: ListNode):
    curr = head
    while curr != None:
        print(curr.val, end=" -> ")
        curr = curr.next

    print("None\n")


def main():
    # declaration and input
    s = Solution()
    head = ListNode(None)
    curr = head

    num = input("Enter numbers, -1 to stop: ")
    while num != "-1":
        try:
            num = int(num)
            if curr.val is None:
                head.val = num
            else:
                curr.next = ListNode(num)
                curr = curr.next
        except ValueError:
            print("Invalid input. Please enter an integer.")

        num = input("Enter numbers, -1 to stop: ")

    print("\nOriginal list: ", end="")
    printList(head)

    # processing
    result = s.deleteDuplicates(head)

    # output
    print("\nResult:")
    printList(result)


if __name__ == "__main__":
    main()
