from typing import List


class Solution:
    def getRow(self, rowIndex: int, row=[1]) -> List[int]:
        return (
            self.getRow(rowIndex - 1, [a + b for a, b in zip([0] + row, row + [0])])
            if rowIndex
            else row
        )


def main():
    # declaration
    s = Solution()

    # input
    row = int(input("Enter the row: "))

    # processing
    res = s.getRow(row)

    # output
    print("\nResult:")
    print(res)


if __name__ == "__main__":
    main()
