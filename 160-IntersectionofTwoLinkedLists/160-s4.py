# Time Limit Exceeded
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        stackA = list()
        stackB = list()

        while headA or headB:
            if headA:
                stackA.append(headA)
                headA = headA.next
            if headB:
                stackB.append(headB)
                headB = headB.next

        prev = None
        while stackA and stackB:
            nodeA = stackA.pop(-1)
            nodeB = stackB.pop(-1)

            if nodeA != nodeB:
                return prev
            prev = nodeA


def constructLinkedList(nums: list) -> ListNode:
    if len(nums) == 0 or nums[0] == -1:
        return None

    head = ListNode(nums[0])
    curr = head
    for i in range(1, len(nums)):
        curr.next = ListNode(nums[i])
        curr = curr.next

    return head


def constructIntersectedLinkedList(
    headA: ListNode, headB: ListNode, intersectVal: int, skipA: int, skipB: int
) -> None:

    if intersectVal:
        currA = headA
        for _ in range(skipA):
            currA = currA.next
        currB = headB
        for _ in range(skipB):
            currB = currB.next
        currB.next = currA.next


def printLinkedlist(head: ListNode):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()


def main():
    # declaration
    s = Solution()

    # input
    numsA = input(
        "Enter the values to construct the linked list (separated by spaces): "
    ).split()
    numsA = [int(n) for n in numsA]
    numsB = input(
        "Enter the values to construct the linked list (separated by spaces): "
    ).split()
    numsB = [int(n) for n in numsB]

    intersectVal = int(input("\nEnter the intersect value: "))
    skipA = int(input("Enter the skipA value: "))
    skipB = int(input("Enter the skipB value: "))

    headA = constructLinkedList(numsA)
    headB = constructLinkedList(numsB)

    constructIntersectedLinkedList(headA, headB, intersectVal, skipA, skipB)

    # processing
    res = s.getIntersectionNode(headA, headB)

    # output
    print("\n\nResult:")
    if res != None:
        print("Intersected at '", res.val, "'\n", sep="")
    else:
        print("No intersection")


if __name__ == "__main__":
    main()
