from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        beginning = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[beginning], nums[i] = nums[i], nums[beginning]
                beginning += 1


def main():
    # declaration and input
    s = Solution()
    nums = input("Enter numbers (seperated by space): ").split()
    nums = [int(n) for n in nums]

    # processing
    s.moveZeroes(nums)

    # output
    print("\nResult:")
    print(nums)


if __name__ == "__main__":
    main()
