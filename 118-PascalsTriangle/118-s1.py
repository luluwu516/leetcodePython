from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows < 1:
            return [[]]

        prev_row = [0, 1, 0]

        res = [[1]]
        for i in range(1, numRows):
            curr_row = []
            for j in range(i + 1):
                curr_row.append(prev_row[j] + prev_row[j + 1])
            prev_row = [0]
            prev_row.extend(curr_row)
            prev_row.append(0)
            res.append(curr_row)

        return res


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
