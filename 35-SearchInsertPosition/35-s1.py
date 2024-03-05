from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)

        for n in nums:
            if n > target:
                return nums.index(n)
        return len(nums)


def main():
    # declaration and input
    s = Solution()
    nums = input("Enter numbers for a list separated by spaces: ").split()
    nums = [int(i) for i in nums]
    target = int(input("Enter the target: "))

    # processing
    index = s.searchInsert(nums, target)

    # output
    print("\nResult: ")
    print('The target "', target, '" should be inserted at index ', index, sep="")


if __name__ == "__main__":
    main()
