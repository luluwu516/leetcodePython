from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                row[j] += row[j - 1]
        return row


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
