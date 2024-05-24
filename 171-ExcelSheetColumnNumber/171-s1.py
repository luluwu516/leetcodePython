class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        sum = 0
        for c in columnTitle:
            sum = sum * 26 + (ord(c) - 65 + 1)

        return sum


def main():
    # declaration
    s = Solution()

    # input
    columnTitle = input("Enter the column title: ")

    # processing
    res = s.titleToNumber(columnTitle)

    # output
    print("\nResult:")
    print(f"The column number is '{res}'")


if __name__ == "__main__":
    main()
