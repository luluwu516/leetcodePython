from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sumOfList = int((n * (1 + n)) / 2)  # 1+2+3+...+n

        return sumOfList - sum(nums)


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
