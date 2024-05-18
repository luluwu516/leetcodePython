class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber == 0:
            return ""

        return self.convertToTitle((columnNumber - 1) // 26) + chr(
            ord("A") + ((columnNumber - 1) % 26)
        )
        # columnNumber, remainder = divmod(columnNumber - 1, 26)
        # return self.convertToTitle(columnNumber) + chr(65 + remainder)


def main():
    # declaration and input
    s = Solution()
    columnNumber = int(input("Enter the column number: "))

    # processing
    res = s.convertToTitle(columnNumber)

    # output
    print("\nResult:")
    print(f"The corresponding column title is '{res}'")


if __name__ == "__main__":
    main()
