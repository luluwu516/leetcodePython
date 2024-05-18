class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        temp = columnNumber
        while temp > 0:
            res = chr(ord("A") + ((temp - 1) % 26)) + res
            temp = (temp - 1) // 26

        return res


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
