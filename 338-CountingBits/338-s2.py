from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        for i in range(1, n + 1):
            res.append(1 + res[i & i - 1])

        return res


def main():
    # declaration and input
    s = Solution()
    num = int(input("\nEnter an integer: "))

    # processing
    res = s.countBits(num)

    # output
    print("\nResult:")
    print(res)


if __name__ == "__main__":
    main()
