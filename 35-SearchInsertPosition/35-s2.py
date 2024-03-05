from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left


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
