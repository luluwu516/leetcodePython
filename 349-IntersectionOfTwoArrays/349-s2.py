from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        s1 = set(nums1)
        s2 = set(nums2)
        for n in s1:
            if n in s2:
                res.append(n)

        return res


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
