from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        nums_set = set(nums)
        numbers_set = set(range(0, length + 1))

        return numbers_set.difference(nums_set).pop()


def main():
    # declaration and input
    s = Solution()
    num = input("Enter integers (separated by spaces): ").split()
    num = [int(n) for n in num]

    # processing
    res = s.missingNumber(num)

    # output
    print("\nResult:")
    print("The missing integer is", res)


if __name__ == "__main__":
    main()
