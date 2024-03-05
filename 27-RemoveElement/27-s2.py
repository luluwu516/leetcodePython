from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not len(nums):
            return 0

        while val in nums:
            nums.remove(val)

        return len(nums)


def main():
    # declaration and input
    s = Solution()
    nums = input("Enter values for a list separated by spaces: ").split()
    nums = [int(val) for val in nums]
    val = int(input("Enter the element to remove: "))

    # processing
    k = s.removeElement(nums, val)
    nums = nums[:k]

    # output
    print("\nResult:", k, "duplicates and nums =", nums)


if __name__ == "__main__":
    main()
