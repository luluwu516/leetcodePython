from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums1.sort()
        nums2.sort()
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1

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
