from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_num_count = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[unique_num_count] = nums[i]
                unique_num_count += 1

        return unique_num_count


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
