class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9

        # if num == 0:
        #     return 0
        # else:
        #     return 1 + (num - 1) % 9


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
