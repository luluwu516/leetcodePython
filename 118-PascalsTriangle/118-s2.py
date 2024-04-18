from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return [[]]
        if numRows == 1:
            return [[1]]

        prev_rows = self.generate(numRows - 1)
        new_row = [1] * numRows

        for i in range(1, numRows - 1):
            new_row[i] = prev_rows[-1][i - 1] + prev_rows[-1][i]

        prev_rows.append(new_row)

        return prev_rows


def main():
    # declaration
    s = Solution()

    # input
    row = int(input("Enter the row: "))

    # processing
    res = s.generate(row)

    # output
    print("\nResult:")
    print(res)


if __name__ == "__main__":
    main()
