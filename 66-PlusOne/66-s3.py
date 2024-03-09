from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ""

        for d in digits:
            string += str(d)

        num = int(string) + 1
        result = [int(s) for s in str(num)]

        return result


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
