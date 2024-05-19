from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        median = int(len(nums) / 2)
        return nums[median]


def main():
    # declaration
    s = Solution()

    # input
    nums = input("Enter the numbers (seperated by comma): ").split(",")
    nums = [int(n) for n in nums]

    # processing
    res = s.majorityElement(nums)

    # output
    print("\nResult:")
    print(f"The majority element is {res}")


if __name__ == "__main__":
    main()
