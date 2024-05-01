from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set(nums)
        temp = list(nums)

        for n in s:
            if n in temp:
                temp.remove(n)
            if not (n in temp):
                return n


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
