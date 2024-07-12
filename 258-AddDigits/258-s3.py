class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num

        return self.addDigits(sum([int(c) for c in str(num)]))


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
