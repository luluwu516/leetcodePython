class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 2 == 0:
            n /= 2
        while n % 3 == 0:
            n /= 3
        while n % 5 == 0:
            n /= 5
        return n == 1

        # if n <= 0:
        #     return False
        # for p in [2, 3, 5]:
        #     while n % p == 0:
        #         n = n // p
        # return n == 1


def main():
    # declaration and input
    s = Solution()
    num = int(input("Enter an integer: "))

    # processing
    res = s.isUgly(num)

    # output
    print("\nResult:")
    print(f"The integer is{'' if res else ' not'} an ugly number")


if __name__ == "__main__":
    main()
