from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(str(i) for i in digits))
        num += 1
        nums = [int(i) for i in list(str(num))]
        return nums


def main():
    # declaration and input
    s = Solution()
    nums = input("Enter a list of numbers seperate by space: ").split(",")
    nums = [int(n) for n in nums]

    # processing
    result = s.plusOne(nums)

    # output
    print("\nResult:")
    print("The nums plus one is:", result)


if __name__ == "__main__":
    main()
