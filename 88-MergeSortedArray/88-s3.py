from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1[m:] = nums2
        nums1.sort()

        # nums3 = []
        # for i in range(m):
        #     nums3.append(nums1[i])
        # for i in range(n):
        #     nums3.append(nums2[i])

        # nums3.sort()
        # for i in range(len(nums3)):
        #     nums1[i] = nums3[i]


def main():
    # declaration and input
    s = Solution()
    nums1 = []
    nums2 = []

    print("nums1:")
    num = input("Enter numbers to num1, -1 to stop: ")
    while num != "-1":
        try:
            num = int(num)
            nums1.append(num)
        except ValueError:
            print("Invalid input. Please enter an integer.")

        num = input("Enter numbers to num1, -1 to stop: ")

    print("\nnums2:")
    num = input("Enter numbers to num2, -1 to stop: ")
    while num != "-1":
        try:
            num = int(num)
            nums2.append(num)
        except ValueError:
            print("Invalid input. Please enter an integer.")

        num = input("Enter numbers to num2, -1 to stop: ")

    # nums1 = [1, 2, 3, 0, 0, 0]
    # nums2 = [2, 5, 6]
    print("\nOriginal list: ")
    print("nums1: ", nums1)
    print("nums2: ", nums2)

    # processing
    s.merge(nums1, 3, nums2, 3)

    # output
    print("\nResult:")
    print("Sorted list:", nums1)


if __name__ == "__main__":
    main()
