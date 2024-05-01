from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for i in nums:
            xor = xor ^ i
            # print(xor, i)

        return xor

    # [2,2,1,3,3]
    # Output:
    # 2 2
    # 0 2
    # 1 1
    # 2 3
    # 1 3


def main():
    # declaration
    s = Solution()

    # input
    nums = input("Enter the numbers (seperated by comma): ").split(",")
    nums = [int(n) for n in nums]

    # processing
    res = s.singleNumber(nums)

    # output
    print("\nResult:")
    print("Number", res, "only appears one time")


if __name__ == "__main__":
    main()
