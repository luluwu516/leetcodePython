from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            num = i
            count = 0
            while num > 0:
                num = num & (num - 1)
                count += 1
            res.append(count)

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
