class Solution:
    def addDigits(self, num: int) -> int:
        total = num
        while num > 9:
            total = 0
            total += num % 10
            num //= 10
            while num > 0:
                total += num % 10
                num //= 10
            num = total

        return total


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
