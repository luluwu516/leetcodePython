from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # return set(nums1).intersection(set(nums2))
        return set(nums1) & set(nums2)


def main():
    # declaration and input
    s = Solution()
    nums1 = input("Enter numbers for array 1 (seperated with space): ").split()
    nums1 = [int(n) for n in nums1]
    nums2 = input("Enter numbers for array 2 (seperated with space): ").split()
    nums2 = [int(n) for n in nums2]

    # processing
    res = s.intersection(nums1, nums2)

    # output
    print("\nResult:")
    print("The intersection of two integer arrays is:", res)


if __name__ == "__main__":
    main()
