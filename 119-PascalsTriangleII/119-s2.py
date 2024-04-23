from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        val = 1
        for i in range(1, rowIndex + 1):
            val *= rowIndex + 1 - i
            val /= i
            row.append(int(val))

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
