from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        res = 0
        for i in range(1, length + 1):
            res ^= i
        for num in nums:
            res ^= num

        return res


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
