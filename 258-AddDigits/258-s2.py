class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            nums = [int(c) for c in str(num)]
            num = sum(nums)

        return num


def main():
    # declaration and input
    s = Solution()
    num = int(input("Enter a number: "))

    # processing
    res = s.addDigits(num)

    # output
    print(
        "\nAfter repeatedly adding all its digits until the result has only one digit:"
    )
    print("Result:", res)


if __name__ == "__main__":
    main()
