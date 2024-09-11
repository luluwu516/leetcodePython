from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash = dict()
        res = []
        for n1 in nums1:
            hash[n1] = hash.get(n1, 0) + 1
        for n2 in nums2:
            if n2 in hash and hash[n2] > 0:
                res.append(n2)
                hash[n2] -= 1

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
