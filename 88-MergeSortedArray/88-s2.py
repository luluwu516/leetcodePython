from typing import List


# To accommodate this, nums1 has a length of m + n, where the first m elements
# denote the elements that should be merged, and the last n elements are set to 0
# and should be ignored. nums2 has a length of n.


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return nums1

        i = 0
        while m < len(nums1) and i < n:
            nums1[m] = nums2[i]
            m += 1
            i += 1
        nums1.sort()


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
    # nums2 = [2]
    print("\nOriginal list: ")
    print("nums1: ", nums1)
    print("nums2: ", nums2)

    # processing
    s.merge(nums1, 3, nums2, 1)

    # output
    print("\nResult:")
    print("Sorted list:", nums1)


if __name__ == "__main__":
    main()
