from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        stack = []
        dup_count = 0
        for n in nums:
            if n not in stack:
                stack.append(n)
            else:
                dup_count += 1

        unique = len(nums) - dup_count
        for i in range(unique):
            nums[i] = stack[i]

        return unique


def main():
    # declaration and input
    s = Solution()
    nums = input("Enter values for a list separated by spaces: ").split()
    nums = [int(val) for val in nums]
    expected_nums = []

    # processing
    k = s.removeDuplicates(nums)

    for i in range(k):
        expected_nums.append(nums[i])

    # output
    print("\nResult:", k, "duplicates, the unique numbers:", expected_nums)


if __name__ == "__main__":
    main()
