from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev_row = [0, 1, 0]

        tri = [[1]]
        for i in range(1, rowIndex + 1):
            curr_row = []
            for j in range(i + 1):
                curr_row.append(prev_row[j] + prev_row[j + 1])
            prev_row = [0]
            prev_row.extend(curr_row)
            prev_row.append(0)
            tri.append(curr_row)

        return tri[rowIndex]


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
