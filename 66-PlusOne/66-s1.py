from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                break

        if digits[0] == 0:
            digits.insert(0, 1)

        return digits


def main():
    # declaration and input
    s = Solution()
    nums = input("Enter a list of numbers seperate by space: ").split()
    nums = [int(n) for n in nums]

    # processing
    result = s.plusOne(nums)

    # output
    print("\nResult:")
    print("The nums plus one is:", result)


if __name__ == "__main__":
    main()
