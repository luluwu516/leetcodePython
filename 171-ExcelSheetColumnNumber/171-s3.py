class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        rcolumnTitle = columnTitle[::-1]
        sum = 0
        for unit in range(len(rcolumnTitle)):
            sum += (ord(rcolumnTitle[unit]) - 65 + 1) * pow(26, unit)

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
