from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        counter = Counter(nums1)

        for n2 in nums2:
            if n2 in counter and counter[n2] > 0:
                res.append(n2)
                counter[n2] -= 1

        return res


def main():
    # declaration and input
    s = Solution()
    nums1 = input("Enter numbers for array 1 (seperated with space): ").split()
    nums1 = [int(n) for n in nums1]
    nums2 = input("Enter numbers for array 2 (seperated with space): ").split()
    nums2 = [int(n) for n in nums2]

    # processing
    res = s.intersect(nums1, nums2)

    # output
    print("\nResult:")
    print("The intersection of two integer arrays is:", res)


if __name__ == "__main__":
    main()
