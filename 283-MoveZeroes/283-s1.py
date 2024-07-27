from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)


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
