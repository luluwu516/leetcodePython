from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode(0)
        current = head

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return head.next


def create_linked_list(values):
    head = ListNode()
    current = head
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return head.next


def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print("]")


def main():
    # declaration
    s = Solution()

    # input
    print("\nList 1")
    list1_values = input("Enter values for list1 separated by spaces: ").split()
    list1_values = [int(val) for val in list1_values]

    print("\nList 2")
    list2_values = input("Enter values for list1 separated by spaces: ").split()
    list2_values = [int(val) for val in list2_values]

    list1 = create_linked_list(list1_values)
    list2 = create_linked_list(list2_values)

    # processing
    merged = s.mergeTwoLists(list1, list2)

    # output
    print("\Input:")
    print("\nList 1:", list1_values)
    print("List 2:", list2_values)

    print("\nResult:")
    print("Merged List: ", end="")
    print_linked_list(merged)
    print()


if __name__ == "__main__":
    main()
