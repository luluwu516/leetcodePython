from typing import List


# Time Limit Exceeded
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for n in nums:
            if nums.count(n) > 1:
                return True
        return False


def main():
    # declaration
    s = Solution()

    # input
    nums = input("Enter the numbers (seperated by comma): ").split(",")
    nums = [int(n) for n in nums]

    # processing
    res = s.containsDuplicate(nums)

    # output
    print("\nResult:")
    print("The array", ("contains" if res else "doesn't contain"), "duplicate")


if __name__ == "__main__":
    main()
