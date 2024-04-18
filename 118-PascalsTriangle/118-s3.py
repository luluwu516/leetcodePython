from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    prev_row = res[i - 1]
                    row.append(prev_row[j - 1] + prev_row[j])

            res.append(row)

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
